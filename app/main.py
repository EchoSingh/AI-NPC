from fastapi import FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import uuid
from contextlib import asynccontextmanager

from app.models import (
    NPCCreate, NPCResponse, Message, ChatResponse, 
    Quest, QuestRequest, MemoryEntry
)
from app.memory import MemoryManager
from app.personality import PersonalityEngine
from app.llm_service import LLMService


# Lifespan context manager for startup/shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 Starting AI NPC System...")
    yield
    # Shutdown
    print("👋 Shutting down AI NPC System...")


app = FastAPI(
    title="AI NPC System",
    description="Intelligent NPCs for RPG/Open World Games with memory and personality",
    version="1.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize services
memory_manager = MemoryManager()
llm_service = LLMService()


@app.get("/", tags=["Root"])
async def root():
    """Health check endpoint"""
    return {
        "status": "online",
        "message": "AI NPC System is running",
        "version": "1.0.0"
    }


@app.post("/npc", response_model=NPCResponse, status_code=status.HTTP_201_CREATED, tags=["NPC Management"])
async def create_npc(npc: NPCCreate):
    """Create a new NPC with personality and background"""
    
    # Check if NPC already exists
    existing = memory_manager.get_npc(npc.npc_id)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"NPC with id '{npc.npc_id}' already exists"
        )
    
    # Create NPC response
    npc_response = NPCResponse(
        npc_id=npc.npc_id,
        name=npc.name,
        personality=npc.personality,
        background=npc.background,
        location=npc.location,
        conversation_count=0
    )
    
    # Store in memory
    success = memory_manager.store_npc(npc_response)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to store NPC"
        )
    
    return npc_response


@app.get("/npc/{npc_id}", response_model=NPCResponse, tags=["NPC Management"])
async def get_npc(npc_id: str):
    """Get NPC details"""
    npc = memory_manager.get_npc(npc_id)
    if not npc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with id '{npc_id}' not found"
        )
    
    # Get conversation count
    conv_count = memory_manager.get_conversation_count(npc_id)
    npc["conversation_count"] = conv_count
    
    return npc


@app.delete("/npc/{npc_id}", tags=["NPC Management"])
async def delete_npc(npc_id: str):
    """Delete an NPC"""
    npc = memory_manager.get_npc(npc_id)
    if not npc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with id '{npc_id}' not found"
        )
    
    success = memory_manager.delete_npc(npc_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to delete NPC"
        )
    
    return {"message": f"NPC '{npc_id}' deleted successfully"}


@app.post("/chat", response_model=ChatResponse, tags=["Interaction"])
async def chat_with_npc(message: Message):
    """Chat with an NPC - the main interaction endpoint"""
    
    # Get NPC data
    npc = memory_manager.get_npc(message.npc_id)
    if not npc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with id '{message.npc_id}' not found"
        )
    
    # Get conversation history
    history = memory_manager.get_conversation_history(
        message.player_id, 
        message.npc_id,
        limit=10
    )
    
    # Get player reputation
    reputation = memory_manager.get_player_reputation(
        message.player_id,
        message.npc_id
    )
    
    # Generate system prompt
    system_prompt = PersonalityEngine.get_system_prompt(
        personality=npc["personality"],
        npc_name=npc["name"],
        background=npc["background"],
        location=npc["location"],
        reputation=reputation
    )
    
    # Convert history to dict format
    history_dict = [
        {
            "player_message": entry.player_message,
            "npc_response": entry.npc_response
        }
        for entry in history
    ]
    
    # Generate response using LLM
    npc_response_text = await llm_service.generate_response(
        system_prompt=system_prompt,
        user_message=message.message,
        conversation_history=history_dict
    )
    
    # Calculate reputation change
    rep_change = PersonalityEngine.calculate_reputation_change(
        personality=npc["personality"],
        player_message=message.message
    )
    new_reputation = reputation + rep_change
    memory_manager.store_player_reputation(
        message.player_id,
        message.npc_id,
        new_reputation
    )
    
    # Store conversation
    memory_manager.store_conversation(
        player_id=message.player_id,
        npc_id=message.npc_id,
        player_message=message.message,
        npc_response=npc_response_text,
        context={"reputation": str(new_reputation)}
    )
    
    # Increment conversation count
    memory_manager.increment_conversation_count(message.npc_id)
    
    return ChatResponse(
        npc_response=npc_response_text,
        npc_emotion=npc["personality"],
        quest_offered=False
    )


@app.get("/history/{player_id}/{npc_id}", response_model=List[MemoryEntry], tags=["Interaction"])
async def get_conversation_history(player_id: str, npc_id: str, limit: int = 20):
    """Get conversation history between player and NPC"""
    history = memory_manager.get_conversation_history(player_id, npc_id, limit)
    return history


@app.post("/quest/generate", response_model=Quest, tags=["Quests"])
async def generate_quest(quest_request: QuestRequest):
    """Generate a quest from an NPC"""
    
    # Get NPC data
    npc = memory_manager.get_npc(quest_request.npc_id)
    if not npc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"NPC with id '{quest_request.npc_id}' not found"
        )
    
    # Generate quest using LLM
    quest_data = await llm_service.generate_quest(
        npc_name=npc["name"],
        npc_background=npc["background"],
        personality=npc["personality"],
        player_context=quest_request.context
    )
    
    # Create quest object
    quest = Quest(
        quest_id=str(uuid.uuid4()),
        title=quest_data.get("title", "Unknown Quest"),
        description=quest_data.get("description", ""),
        difficulty=quest_data.get("difficulty", "medium"),
        reward=quest_data.get("reward", "Unknown"),
        objectives=quest_data.get("objectives", [])
    )
    
    return quest


@app.get("/reputation/{player_id}/{npc_id}", tags=["Interaction"])
async def get_reputation(player_id: str, npc_id: str):
    """Get player reputation with an NPC"""
    reputation = memory_manager.get_player_reputation(player_id, npc_id)
    
    # Determine reputation level
    if reputation > 50:
        level = "Trusted Ally"
    elif reputation > 0:
        level = "Friendly"
    elif reputation == 0:
        level = "Neutral"
    elif reputation > -50:
        level = "Disliked"
    else:
        level = "Enemy"
    
    return {
        "player_id": player_id,
        "npc_id": npc_id,
        "reputation": reputation,
        "level": level
    }


if __name__ == "__main__":
    import uvicorn
    from app.config import get_settings
    
    settings = get_settings()
    uvicorn.run(
        "app.main:app",
        host=settings.api_host,
        port=settings.api_port,
        reload=True
    )
