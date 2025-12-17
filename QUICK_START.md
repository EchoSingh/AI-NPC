# Quick Reference Card

## 🎮 Your AI NPC System is READY!

### ✅ What You Have
- ✨ **6 Personality Types**: Friendly, Aggressive, Mysterious, Merchant, Wise, Comedic
- 🧠 **Smart Memory**: Redis-powered conversation history & reputation
- 🗺️ **Quest Generator**: AI-generated quests
- 🐳 **Docker Ready**: Fully containerized
- 📚 **Complete Docs**: README, API docs, examples, deployment guide

### 🚀 Quick Commands

```bash
# Start project
docker-compose up -d

# Stop project
docker-compose down

# View logs
docker-compose logs -f api

# Test API
curl http://localhost:8000

# Chat with NPC
curl -X POST http://localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{"player_id":"hero_001","npc_id":"blacksmith_thorin","message":"Hello!"}'
```

### 📦 Push to GitHub (3 steps)

1. **Create repo** on GitHub: https://github.com/new
   - Name: `NPC`
   - Public
   - Don't initialize with README

2. **Add remote and push**:
```bash
git remote add origin https://github.com/EchoSingh/NPC.git
git branch -M main
git push -u origin main
```

3. **Add topics** on GitHub repo page:
   `ai`, `npc`, `rpg`, `game-development`, `fastapi`, `llm`, `openai`, `redis`, `docker`, `python`

### 🐳 Push to Docker Hub (3 steps)

1. **Login**:
```bash
docker login
# Username: aditya26062003
```

2. **Build**:
```bash
docker build -t aditya26062003/ai-npc-system:latest -t aditya26062003/ai-npc-system:1.0.0 .
```

3. **Push**:
```bash
docker push aditya26062003/ai-npc-system:latest
docker push aditya26062003/ai-npc-system:1.0.0
```

### 🔗 Your Links

- **GitHub**: https://github.com/EchoSingh/NPC
- **Docker Hub**: https://hub.docker.com/u/aditya26062003
- **Local API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

### 🎯 Demo Mode vs Real LLM

**Current: Demo Mode** (No API key needed)
- Returns mock responses
- Perfect for testing
- Works immediately

**To enable real LLM**:

**Option A: OpenAI** (Paid, best quality)
```bash
# Edit .env
DEMO_MODE=false
OPENAI_API_KEY=sk-your-real-key-here
USE_OLLAMA=false

# Restart
docker-compose restart api
```

**Option B: Ollama** (Free, local)
```bash
# Install Ollama
curl https://ollama.ai/install.sh | sh
ollama pull llama2

# Edit .env
DEMO_MODE=false
USE_OLLAMA=true

# Restart
docker-compose restart api
```

### 📊 Test All NPCs

```bash
# Friendly Blacksmith
curl -X POST http://localhost:8000/chat -H 'Content-Type: application/json' \
  -d '{"player_id":"hero","npc_id":"blacksmith_thorin","message":"Can you make me a sword?"}'

# Aggressive Guard
curl -X POST http://localhost:8000/chat -H 'Content-Type: application/json' \
  -d '{"player_id":"hero","npc_id":"guard_brutus","message":"Let me pass"}'

# Mysterious Oracle
curl -X POST http://localhost:8000/chat -H 'Content-Type: application/json' \
  -d '{"player_id":"hero","npc_id":"oracle_mystara","message":"Tell me my future"}'

# Merchant
curl -X POST http://localhost:8000/chat -H 'Content-Type: application/json' \
  -d '{"player_id":"hero","npc_id":"merchant_pete","message":"What do you sell?"}'
```

### 🎉 Make it Trending

1. **Add a demo GIF** to README
2. **Star your own repo**
3. **Share on**:
   - Reddit: r/gamedev, r/programming
   - Twitter/X: #gamedev #AI #IndieGame
   - Dev.to / Hashnode

### 🆘 Need Help?

See full guides:
- [README.md](README.md) - Main documentation
- [API.md](API.md) - Complete API reference
- [DEPLOYMENT.md](DEPLOYMENT.md) - Detailed deployment guide
- [EXAMPLES.md](EXAMPLES.md) - More NPC examples

---

**Made with ❤️ by [@EchoSingh](https://github.com/EchoSingh)**

🔥 **This will look AMAZING on your GitHub profile!** 🔥
