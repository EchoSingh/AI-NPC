from typing import Optional, Dict, List
import json
from openai import OpenAI
import httpx
from app.config import get_settings
from app.models import PersonalityType


class LLMService:
    """Service to interact with OpenAI or Ollama LLMs"""
    
    def __init__(self):
        self.settings = get_settings()
        self.demo_mode = self.settings.demo_mode
        
        if self.demo_mode:
            self.client_type = "demo"
        elif self.settings.use_ollama:
            self.client_type = "ollama"
            self.base_url = self.settings.ollama_base_url
            self.model = self.settings.ollama_model
        else:
            self.client_type = "openai"
            self.client = OpenAI(api_key=self.settings.openai_api_key)
            self.model = self.settings.openai_model
    
    async def generate_response(
        self,
        system_prompt: str,
        user_message: str,
        conversation_history: Optional[List[Dict[str, str]]] = None
    ) -> str:
        """Generate LLM response"""
        
        # Demo mode - return mock response
        if self.demo_mode:
            return self._generate_demo(system_prompt, user_message)
        
        messages = [{"role": "system", "content": system_prompt}]
        
        # Add conversation history (last 5 exchanges)
        if conversation_history:
            for entry in reversed(conversation_history[-5:]):
                messages.append({"role": "user", "content": entry.get("player_message", "")})
                messages.append({"role": "assistant", "content": entry.get("npc_response", "")})
        
        # Add current message
        messages.append({"role": "user", "content": user_message})
        
        if self.client_type == "ollama":
            return await self._generate_ollama(messages)
        else:
            return await self._generate_openai(messages)
    
    def _generate_demo(self, system_prompt: str, user_message: str) -> str:
        """Generate demo response based on personality"""
        responses = {
            "friendly": f"Hello there, friend! I heard you say: '{user_message[:30]}...' I'd be happy to help you with that! This is a demo response - connect a real LLM for full conversations.",
            "aggressive": f"What do you want? You said something about '{user_message[:30]}...' Make it quick! (Demo mode active)",
            "mysterious": f"Interesting... your words echo with meaning: '{user_message[:30]}...' Perhaps the answer lies beyond what you seek... (Demo response)",
            "merchant": f"Ah, a customer! You mentioned '{user_message[:30]}...' I have just what you need! The finest goods at reasonable prices. (Demo mode)",
            "wise": f"Young one, you speak of '{user_message[:30]}...' Let me share some wisdom with you about this matter... (Demo response)",
            "comedic": f"Ha! You said '{user_message[:30]}...' That reminds me of a joke! Why did the NPC cross the road? To get to the other script! (Demo mode)"
        }
        
        # Extract personality from system prompt
        for personality, response in responses.items():
            if personality.upper() in system_prompt:
                return response
        
        return f"Greetings! You said: '{user_message[:50]}...' (Demo mode - configure OpenAI or Ollama for real responses)"
    
    async def _generate_openai(self, messages: List[Dict[str, str]]) -> str:
        """Generate response using OpenAI"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=200,
                temperature=0.8
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            print(f"OpenAI Error: {e}")
            return "I seem to be at a loss for words right now..."
    
    async def _generate_ollama(self, messages: List[Dict[str, str]]) -> str:
        """Generate response using Ollama"""
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.post(
                    f"{self.base_url}/api/chat",
                    json={
                        "model": self.model,
                        "messages": messages,
                        "stream": False
                    }
                )
                response.raise_for_status()
                result = response.json()
                return result["message"]["content"].strip()
        except Exception as e:
            print(f"Ollama Error: {e}")
            return "I seem to be at a loss for words right now..."
    
    async def generate_quest(
        self,
        npc_name: str,
        npc_background: str,
        personality: PersonalityType,
        player_context: Optional[str] = None
    ) -> Dict:
        """Generate a quest for the player"""
        
        prompt = f"""You are {npc_name}, an NPC with the following background: {npc_background}

Your personality is: {personality.value}

Generate a quest that fits your character. The quest should be engaging and appropriate for an RPG game.
{f"Context: {player_context}" if player_context else ""}

Respond in JSON format:
{{
    "title": "Quest Title",
    "description": "Quest description",
    "difficulty": "easy/medium/hard",
    "reward": "Description of reward",
    "objectives": ["Objective 1", "Objective 2"]
}}

Only respond with valid JSON."""
        
        messages = [
            {"role": "system", "content": "You are a quest generator for an RPG game. Always respond with valid JSON."},
            {"role": "user", "content": prompt}
        ]
        
        try:
            if self.client_type == "ollama":
                response_text = await self._generate_ollama(messages)
            else:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=300,
                    temperature=0.7
                )
                response_text = response.choices[0].message.content.strip()
            
            # Extract JSON if wrapped in markdown
            if "```json" in response_text:
                response_text = response_text.split("```json")[1].split("```")[0].strip()
            elif "```" in response_text:
                response_text = response_text.split("```")[1].split("```")[0].strip()
            
            return json.loads(response_text)
        except Exception as e:
            print(f"Quest generation error: {e}")
            return {
                "title": "A Simple Task",
                "description": f"{npc_name} needs your help with something.",
                "difficulty": "medium",
                "reward": "Gold and experience",
                "objectives": ["Talk to the quest giver", "Complete the task"]
            }
