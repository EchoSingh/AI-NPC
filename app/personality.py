from typing import List, Dict
from app.config import get_settings
from app.models import PersonalityType


class PersonalityEngine:
    """Handles NPC personality traits and conversation styles"""
    
    PERSONALITY_PROMPTS = {
        PersonalityType.FRIENDLY: {
            "traits": "warm, helpful, enthusiastic, and cheerful",
            "speaking_style": "Use friendly greetings, exclamation marks, and show genuine interest in the player",
            "example": "Oh hello there, friend! How wonderful to see you!"
        },
        PersonalityType.AGGRESSIVE: {
            "traits": "hostile, short-tempered, confrontational, and intimidating",
            "speaking_style": "Use harsh words, threats, and show distrust. Be direct and unfriendly",
            "example": "What do YOU want? Make it quick before I lose my patience."
        },
        PersonalityType.MYSTERIOUS: {
            "traits": "cryptic, enigmatic, secretive, and philosophical",
            "speaking_style": "Speak in riddles, hints, and vague statements. Be thought-provoking",
            "example": "The paths we walk are not always as they seem... What brings you to my shadows?"
        },
        PersonalityType.MERCHANT: {
            "traits": "business-minded, shrewd, opportunistic, and persuasive",
            "speaking_style": "Focus on deals, prices, and value. Be charming but always seeking profit",
            "example": "Ah, a customer! I have the finest wares in all the land. What catches your eye?"
        },
        PersonalityType.WISE: {
            "traits": "knowledgeable, patient, thoughtful, and mentor-like",
            "speaking_style": "Share wisdom, ask deep questions, and guide rather than tell",
            "example": "Welcome, young one. What knowledge do you seek on your journey?"
        },
        PersonalityType.COMEDIC: {
            "traits": "humorous, witty, playful, and lighthearted",
            "speaking_style": "Make jokes, puns, and keep things fun. Don't take yourself too seriously",
            "example": "Hey there! I'd tell you a joke about NPCs, but you might not get the reference!"
        }
    }
    
    @staticmethod
    def get_system_prompt(
        personality: PersonalityType,
        npc_name: str,
        background: str,
        location: str,
        reputation: int = 0
    ) -> str:
        """Generate system prompt based on personality"""
        # Handle both enum and string personalities
        if isinstance(personality, str):
            personality = PersonalityType(personality)
        
        personality_info = PersonalityEngine.PERSONALITY_PROMPTS.get(personality)
        
        reputation_context = ""
        if reputation > 50:
            reputation_context = "The player is a trusted friend and ally."
        elif reputation > 0:
            reputation_context = "The player is known to you, but not yet fully trusted."
        elif reputation < -50:
            reputation_context = "The player is an enemy or has wronged you significantly."
        elif reputation < 0:
            reputation_context = "The player has a poor reputation with you."
        else:
            reputation_context = "The player is a stranger to you."
        
        prompt = f"""You are {npc_name}, an NPC in a fantasy RPG game.

PERSONALITY: {personality.value.upper()}
You are {personality_info['traits']}.

BACKGROUND: {background}

LOCATION: {location}

SPEAKING STYLE: {personality_info['speaking_style']}

RELATIONSHIP: {reputation_context}

GUIDELINES:
- Stay in character at all times
- Keep responses concise (2-4 sentences typically)
- Be immersive and engaging
- Reference your background and location when relevant
- React authentically based on your personality
- Remember previous conversations with the player
- You can offer quests or information naturally in conversation

Example response: {personality_info['example']}

Respond naturally to the player's messages."""
        
        return prompt
    
    @staticmethod
    def calculate_reputation_change(
        personality: PersonalityType,
        player_message: str
    ) -> int:
        """Calculate reputation change based on interaction (simplified)"""
        # Handle both enum and string personalities
        if isinstance(personality, str):
            personality = PersonalityType(personality)
        
        message_lower = player_message.lower()
        
        # Positive keywords
        positive = ["please", "thank", "help", "friend", "honor", "respect"]
        negative = ["fool", "idiot", "stupid", "hate", "attack", "threat"]
        
        change = 0
        
        for word in positive:
            if word in message_lower:
                change += 2
        
        for word in negative:
            if word in message_lower:
                change -= 3
        
        # Personality modifiers
        if personality == PersonalityType.FRIENDLY:
            change += 1  # Friendly NPCs like everyone more
        elif personality == PersonalityType.AGGRESSIVE:
            change -= 1  # Aggressive NPCs harder to please
        
        return max(min(change, 10), -10)  # Cap between -10 and +10
