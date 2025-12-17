# AI NPC System for RPG Games 🎮

**Intelligent NPCs with personality, memory, and dynamic quest generation powered by LLMs**

Create immersive game characters that remember players, have distinct personalities, and generate dynamic quests on-the-fly.

## 🚀 Quick Start

```bash
# Pull the image
docker pull aditya26062003/ai-npc-system:latest

# Create .env file
cat > .env << EOF
OPENAI_API_KEY=your_key_here
DEMO_MODE=true
REDIS_HOST=redis
REDIS_PORT=6379
EOF

# Run with docker-compose
curl -O https://raw.githubusercontent.com/EchoSingh/AI-NPC/main/docker-compose.yml
docker-compose up -d
```

Access API at: **http://localhost:8000**  
API Docs: **http://localhost:8000/docs**

## ✨ Features

- 🧠 **Intelligent Conversations** - Natural language processing via OpenAI or Ollama
- 🎭 **6 Personality Types** - Friendly, Aggressive, Mysterious, Merchant, Wise, Comedic
- 💾 **Persistent Memory** - Redis-powered conversation history and player reputation
- 🗺️ **Dynamic Quests** - AI-generated quests tailored to NPC personality
- 🐳 **Production Ready** - Docker containerization with Redis integration

## 📖 Documentation

**GitHub Repository:** https://github.com/EchoSingh/AI-NPC

Complete docs, examples, and API reference available in the repository.

## 🎯 Quick Test

```bash
# Create an NPC
curl -X POST http://localhost:8000/npc \
  -H "Content-Type: application/json" \
  -d '{
    "npc_id": "blacksmith_01",
    "name": "Thorin",
    "personality": "friendly",
    "background": "A master blacksmith",
    "location": "Town Forge"
  }'

# Chat with the NPC
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "player_id": "player_1",
    "npc_id": "blacksmith_01",
    "message": "Can you make me a sword?"
  }'
```

## 🔧 Configuration

Set `DEMO_MODE=true` for testing without API keys, or configure:
- **OpenAI**: Add `OPENAI_API_KEY` for cloud LLM
- **Ollama**: Set `USE_OLLAMA=true` for local LLM

## 📊 Tech Stack

- FastAPI - Modern Python web framework
- Redis - Persistent memory storage
- OpenAI/Ollama - LLM integration
- Docker - Containerization

## 📝 License

MIT License - See GitHub repository for details

---

**Created by:** [@EchoSingh](https://github.com/EchoSingh)  
**Repository:** https://github.com/EchoSingh/AI-NPC
