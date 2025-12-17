import redis
import json
from typing import List, Optional, Dict
from datetime import datetime
from app.config import get_settings
from app.models import MemoryEntry, NPCResponse


class MemoryManager:
    def __init__(self):
        settings = get_settings()
        self.redis_client = redis.Redis(
            host=settings.redis_host,
            port=settings.redis_port,
            db=settings.redis_db,
            decode_responses=True
        )
    
    def store_npc(self, npc_data: NPCResponse) -> bool:
        """Store NPC data in Redis"""
        key = f"npc:{npc_data.npc_id}"
        try:
            self.redis_client.set(key, npc_data.model_dump_json())
            return True
        except Exception as e:
            print(f"Error storing NPC: {e}")
            return False
    
    def get_npc(self, npc_id: str) -> Optional[Dict]:
        """Retrieve NPC data from Redis"""
        key = f"npc:{npc_id}"
        try:
            data = self.redis_client.get(key)
            if data:
                return json.loads(data)
            return None
        except Exception as e:
            print(f"Error retrieving NPC: {e}")
            return None
    
    def store_conversation(
        self, 
        player_id: str, 
        npc_id: str, 
        player_message: str, 
        npc_response: str,
        context: Dict[str, str] = None
    ) -> bool:
        """Store conversation in Redis"""
        key = f"conversation:{player_id}:{npc_id}"
        
        memory_entry = MemoryEntry(
            timestamp=datetime.now().isoformat(),
            player_message=player_message,
            npc_response=npc_response,
            context=context or {}
        )
        
        try:
            # Store as list, keep last 50 messages
            self.redis_client.lpush(key, memory_entry.model_dump_json())
            self.redis_client.ltrim(key, 0, 49)
            
            # Set expiry for 7 days
            self.redis_client.expire(key, 604800)
            return True
        except Exception as e:
            print(f"Error storing conversation: {e}")
            return False
    
    def get_conversation_history(
        self, 
        player_id: str, 
        npc_id: str, 
        limit: int = 10
    ) -> List[MemoryEntry]:
        """Retrieve conversation history"""
        key = f"conversation:{player_id}:{npc_id}"
        try:
            messages = self.redis_client.lrange(key, 0, limit - 1)
            return [MemoryEntry(**json.loads(msg)) for msg in messages]
        except Exception as e:
            print(f"Error retrieving conversation history: {e}")
            return []
    
    def increment_conversation_count(self, npc_id: str) -> int:
        """Increment and return conversation count for NPC"""
        key = f"npc_stats:{npc_id}:conversations"
        return self.redis_client.incr(key)
    
    def get_conversation_count(self, npc_id: str) -> int:
        """Get total conversation count for NPC"""
        key = f"npc_stats:{npc_id}:conversations"
        count = self.redis_client.get(key)
        return int(count) if count else 0
    
    def store_player_reputation(
        self, 
        player_id: str, 
        npc_id: str, 
        reputation: int
    ) -> bool:
        """Store player reputation with NPC (-100 to 100)"""
        key = f"reputation:{player_id}:{npc_id}"
        try:
            self.redis_client.set(key, reputation)
            return True
        except Exception as e:
            print(f"Error storing reputation: {e}")
            return False
    
    def get_player_reputation(self, player_id: str, npc_id: str) -> int:
        """Get player reputation with NPC"""
        key = f"reputation:{player_id}:{npc_id}"
        reputation = self.redis_client.get(key)
        return int(reputation) if reputation else 0
    
    def delete_npc(self, npc_id: str) -> bool:
        """Delete NPC data"""
        keys = [
            f"npc:{npc_id}",
            f"npc_stats:{npc_id}:conversations"
        ]
        try:
            self.redis_client.delete(*keys)
            return True
        except Exception as e:
            print(f"Error deleting NPC: {e}")
            return False
