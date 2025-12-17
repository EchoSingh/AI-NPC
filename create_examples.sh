#!/bin/bash

# Create example NPCs for testing

API_URL="http://localhost:8000"

echo "🎮 Creating Example NPCs..."
echo ""

# Create Blacksmith
echo "⚒️  Creating Thorin Ironforge (Blacksmith)..."
curl -s -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "blacksmith_thorin",
  "name": "Thorin Ironforge",
  "personality": "friendly",
  "background": "A master blacksmith with 30 years of experience. He has crafted weapons for legendary heroes and loves sharing tales of epic battles.",
  "location": "Town Forge - Market District"
}' | python3 -m json.tool

echo ""

# Create Guard
echo "🛡️  Creating Captain Brutus (Guard)..."
curl -s -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "guard_brutus",
  "name": "Captain Brutus",
  "personality": "aggressive",
  "background": "A battle-hardened veteran who has defended the city gates for 15 years. He trusts no one.",
  "location": "City Gates - North Entrance"
}' | python3 -m json.tool

echo ""

# Create Oracle
echo "🔮 Creating Mystara the Seer (Oracle)..."
curl -s -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "oracle_mystara",
  "name": "Mystara the Seer",
  "personality": "mysterious",
  "background": "An enigmatic prophet who speaks in riddles and seems to know things before they happen.",
  "location": "The Hidden Grove - East Forest"
}' | python3 -m json.tool

echo ""

# Create Merchant
echo "💰 Creating Sly Pete (Merchant)..."
curl -s -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "merchant_pete",
  "name": "Sly Pete",
  "personality": "merchant",
  "background": "A traveling merchant known for having the rarest items at premium prices. Shrewd but fair.",
  "location": "Market Square - Central Bazaar"
}' | python3 -m json.tool

echo ""

# Create Elder
echo "🧙 Creating Elder Aldwin (Wise Elder)..."
curl -s -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "elder_aldwin",
  "name": "Elder Aldwin",
  "personality": "wise",
  "background": "The village elder who has witnessed the rise and fall of kingdoms. Possesses vast knowledge.",
  "location": "Elder Hall - Village Center"
}' | python3 -m json.tool

echo ""

# Create Innkeeper
echo "🍺 Creating Rosie Brightheart (Innkeeper)..."
curl -s -X POST $API_URL/npc -H "Content-Type: application/json" -d '{
  "npc_id": "innkeeper_rosie",
  "name": "Rosie Brightheart",
  "personality": "comedic",
  "background": "A cheerful innkeeper known for terrible jokes and amazing ale. Never lets a sad face stay sad.",
  "location": "The Drunken Dragon Inn"
}' | python3 -m json.tool

echo ""
echo "✅ All NPCs created successfully!"
echo ""
echo "🧪 Test with:"
echo "  curl -X POST $API_URL/chat -H 'Content-Type: application/json' -d '{\"player_id\":\"test_player\",\"npc_id\":\"blacksmith_thorin\",\"message\":\"Hello!\"}'"
