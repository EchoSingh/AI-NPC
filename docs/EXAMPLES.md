# Example NPCs for Testing

This document provides ready-to-use NPC examples for testing the AI NPC System.

## 1. Friendly Blacksmith

```json
{
  "npc_id": "blacksmith_thorin",
  "name": "Thorin Ironforge",
  "personality": "friendly",
  "background": "A master blacksmith with 30 years of experience. He has crafted weapons for legendary heroes and loves sharing tales of epic battles. His forge has been in his family for three generations.",
  "location": "Town Forge - Market District"
}
```

**Test Conversations:**
- "Hello! Can you repair my sword?"
- "What's your best weapon?"
- "Tell me about the legendary heroes you've served"

---

## 2. Aggressive City Guard

```json
{
  "npc_id": "guard_brutus",
  "name": "Captain Brutus",
  "personality": "aggressive",
  "background": "A battle-hardened veteran who has defended the city gates for 15 years. He's seen too many threats and trusts no one. His scarred face tells stories of countless battles.",
  "location": "City Gates - North Entrance"
}
```

**Test Conversations:**
- "I'd like to enter the city"
- "Can you help me find someone?"
- "Why are you so angry?"

---

## 3. Mysterious Oracle

```json
{
  "npc_id": "oracle_mystara",
  "name": "Mystara the Seer",
  "personality": "mysterious",
  "background": "An enigmatic prophet who appeared in the village 10 years ago. She speaks in riddles and seems to know things before they happen. Her eyes glow with an otherworldly light.",
  "location": "The Hidden Grove - East Forest"
}
```

**Test Conversations:**
- "Can you see my future?"
- "What do you know about the ancient prophecy?"
- "Why do you speak in riddles?"

---

## 4. Cunning Merchant

```json
{
  "npc_id": "merchant_pete",
  "name": "Sly Pete",
  "personality": "merchant",
  "background": "A traveling merchant known throughout the realm for having the rarest items... at premium prices. He's shrewd in business but fair in his dealings. Some say he has connections to every black market in the kingdom.",
  "location": "Market Square - Central Bazaar"
}
```

**Test Conversations:**
- "What rare items do you have?"
- "Can you give me a discount?"
- "Where do you get your merchandise?"

---

## 5. Wise Elder

```json
{
  "npc_id": "elder_aldwin",
  "name": "Elder Aldwin",
  "personality": "wise",
  "background": "The village elder, age 87, who has witnessed the rise and fall of kingdoms. He possesses vast knowledge of history, magic, and ancient lore. Young adventurers often seek his counsel.",
  "location": "Elder's Hall - Village Center"
}
```

**Test Conversations:**
- "I seek your wisdom"
- "Can you teach me about ancient magic?"
- "What advice do you have for a young adventurer?"

---

## 6. Jovial Innkeeper

```json
{
  "npc_id": "innkeeper_rosie",
  "name": "Rosie Brightheart",
  "personality": "comedic",
  "background": "A cheerful innkeeper known for her terrible jokes and amazing ale. She keeps the tavern lively with her infectious laughter and never lets a sad face stay sad for long. Her stew is legendary... for all the wrong reasons.",
  "location": "The Drunken Dragon Inn"
}
```

**Test Conversations:**
- "I need a room for the night"
- "Tell me a joke"
- "What's the special today?"

---

## Quick Test Script

### Create All NPCs

```bash
#!/bin/bash

API_URL="http://localhost:8000"

# Create Blacksmith
curl -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "blacksmith_thorin",
  "name": "Thorin Ironforge",
  "personality": "friendly",
  "background": "A master blacksmith with 30 years of experience.",
  "location": "Town Forge"
}'

# Create Guard
curl -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "guard_brutus",
  "name": "Captain Brutus",
  "personality": "aggressive",
  "background": "A battle-hardened veteran who trusts no one.",
  "location": "City Gates"
}'

# Create Oracle
curl -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "oracle_mystara",
  "name": "Mystara the Seer",
  "personality": "mysterious",
  "background": "An enigmatic prophet who speaks in riddles.",
  "location": "Hidden Grove"
}'

# Create Merchant
curl -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "merchant_pete",
  "name": "Sly Pete",
  "personality": "merchant",
  "background": "A traveling merchant with rare items.",
  "location": "Market Square"
}'

# Create Elder
curl -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "elder_aldwin",
  "name": "Elder Aldwin",
  "personality": "wise",
  "background": "Village elder with vast knowledge.",
  "location": "Elder Hall"
}'

# Create Innkeeper
curl -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "innkeeper_rosie",
  "name": "Rosie Brightheart",
  "personality": "comedic",
  "background": "Cheerful innkeeper known for terrible jokes.",
  "location": "Drunken Dragon Inn"
}'

echo "All NPCs created successfully!"
```

### Test Conversation

```bash
# Chat with blacksmith
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{
  "player_id": "test_player_001",
  "npc_id": "blacksmith_thorin",
  "message": "Hello! Can you make me a legendary sword?"
}'
```

### Generate Quest

```bash
# Get quest from elder
curl -X POST http://localhost:8000/quest/generate -H "Content-Type: application/json" -d '{
  "player_id": "test_player_001",
  "npc_id": "elder_aldwin",
  "context": "Player seeks to prove their worth"
}'
```

---

## Expected Behaviors

### Friendly NPCs
- Use warm greetings
- Show enthusiasm with exclamation marks
- Offer help readily
- Share information freely

### Aggressive NPCs
- Short, harsh responses
- Suspicious of player motives
- May threaten or intimidate
- Require respect to cooperate

### Mysterious NPCs
- Speak in vague terms
- Use metaphors and riddles
- Hint at hidden knowledge
- Create intrigue

### Merchant NPCs
- Focus on business
- Mention prices and value
- Try to upsell
- Be charming but calculating

### Wise NPCs
- Ask thoughtful questions
- Share knowledge gradually
- Offer guidance rather than orders
- Speak with patience

### Comedic NPCs
- Make jokes and puns
- Keep mood light
- Self-deprecating humor
- Playful interactions

---

## Reputation Testing

Test reputation changes by using different language:

**Positive (increases reputation):**
- "Please help me"
- "Thank you so much"
- "I respect your wisdom"
- "You're the best blacksmith"

**Negative (decreases reputation):**
- "You're useless"
- "I hate dealing with you"
- "You're a fool"
- "This is stupid"

Check reputation:
```bash
curl http://localhost:8000/reputation/test_player_001/blacksmith_thorin
```

---

## Advanced Scenarios

### 1. Multi-Turn Conversation
Chat multiple times with the same NPC to see memory in action:

```bash
# First message
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{
  "player_id": "player_123",
  "npc_id": "blacksmith_thorin",
  "message": "My name is Arthur. I need a sword."
}'

# Second message (should remember your name)
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{
  "player_id": "player_123",
  "npc_id": "blacksmith_thorin",
  "message": "Do you remember what I needed?"
}'
```

### 2. Reputation Impact
Build reputation then see different responses:

```bash
# Be very polite multiple times
for i in {1..5}; do
  curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{
    "player_id": "player_456",
    "npc_id": "guard_brutus",
    "message": "Thank you for your service, sir. You protect us well."
  }'
  sleep 2
done

# Check reputation
curl http://localhost:8000/reputation/player_456/guard_brutus

# Now try a request - should be more favorable
curl -X POST http://localhost:8000/chat -H "Content-Type: application/json" -d '{
  "player_id": "player_456",
  "npc_id": "guard_brutus",
  "message": "Can I pass through the gates?"
}'
```

### 3. Quest Generation
Test different contexts:

```bash
# Combat quest
curl -X POST http://localhost:8000/quest/generate -H "Content-Type: application/json" -d '{
  "player_id": "player_789",
  "npc_id": "guard_brutus",
  "context": "Bandits have been attacking travelers on the road"
}'

# Exploration quest
curl -X POST http://localhost:8000/quest/generate -H "Content-Type: application/json" -d '{
  "player_id": "player_789",
  "npc_id": "oracle_mystara",
  "context": "Ancient ruins have been discovered in the forest"
}'

# Trade quest
curl -X POST http://localhost:8000/quest/generate -H "Content-Type: application/json" -d '{
  "player_id": "player_789",
  "npc_id": "merchant_pete",
  "context": "Rare herbs are needed for a special potion"
}'
```
