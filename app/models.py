from enum import Enum
from typing import Optional, List, Dict
from pydantic import BaseModel, Field


class PersonalityType(str, Enum):
    FRIENDLY = "friendly"
    AGGRESSIVE = "aggressive"
    MYSTERIOUS = "mysterious"
    MERCHANT = "merchant"
    WISE = "wise"
    COMEDIC = "comedic"


class NPCCreate(BaseModel):
    npc_id: str = Field(..., description="Unique identifier for the NPC")
    name: str = Field(..., description="NPC name")
    personality: PersonalityType = Field(..., description="NPC personality type")
    background: str = Field(..., description="NPC background story")
    location: str = Field(default="Unknown", description="NPC location in game")


class NPCResponse(BaseModel):
    npc_id: str
    name: str
    personality: PersonalityType
    background: str
    location: str
    conversation_count: int = 0


class Message(BaseModel):
    player_id: str = Field(..., description="Unique identifier for the player")
    npc_id: str = Field(..., description="Unique identifier for the NPC")
    message: str = Field(..., description="Player's message to NPC")


class ChatResponse(BaseModel):
    npc_response: str
    npc_emotion: Optional[str] = None
    quest_offered: bool = False


class Quest(BaseModel):
    quest_id: str
    title: str
    description: str
    difficulty: str
    reward: str
    objectives: List[str]


class QuestRequest(BaseModel):
    player_id: str
    npc_id: str
    context: Optional[str] = None


class MemoryEntry(BaseModel):
    timestamp: str
    player_message: str
    npc_response: str
    context: Dict[str, str] = {}
