# 🐳 Docker Hub Setup Instructions

## Step 1: Add Description

1. Go to: https://hub.docker.com/r/aditya26062003/ai-npc-system
2. Click **"Edit Repository Details"** or the pencil icon
3. **Short Description** (100 chars):
   ```
   AI NPC System for RPG games with personality, memory, and quest generation powered by LLMs
   ```

4. **Full Description**: Copy the content from `DOCKER_HUB_DESCRIPTION.md`

## Step 2: Add Category

Click "Add a category" and select:
- **Developer Tools** or **Application Infrastructure**

## Step 3: Update Overview

1. Click on **"Repository overview"** section
2. Click **"Edit"**
3. Paste the content from `DOCKER_HUB_DESCRIPTION.md`

## Step 4: Add Links (Optional)

In the repository settings, you can add:
- **Source Code**: https://github.com/EchoSingh/AI-NPC
- **Documentation**: https://github.com/EchoSingh/AI-NPC#readme
- **Issues**: https://github.com/EchoSingh/AI-NPC/issues

---

## ✅ Quick Copy-Paste Versions

### Short Description (100 chars max):
```
AI NPC System for RPG games with personality, memory, and quest generation powered by LLMs
```

### Alternative Short Descriptions:
```
Intelligent NPCs for games with memory, personality, and dynamic quest generation. FastAPI + Redis + LLM
```

```
Create smart game NPCs that remember players, have unique personalities, and generate quests with AI
```

### Tags/Keywords:
```
ai, npc, rpg, game-development, fastapi, llm, openai, redis, docker, python, machine-learning, chatbot
```

---

## 📸 Suggested Badges/Shields

Add these to your GitHub README:

```markdown
![Docker Pulls](https://img.shields.io/docker/pulls/aditya26062003/ai-npc-system)
![Docker Image Size](https://img.shields.io/docker/image-size/aditya26062003/ai-npc-system)
![Docker Image Version](https://img.shields.io/docker/v/aditya26062003/ai-npc-system)
```

---

## 🎯 What to Highlight

Your Docker Hub page should emphasize:

1. ✅ **Easy to use** - One command to run
2. ✅ **Demo mode** - Works without API keys
3. ✅ **Production ready** - Docker + Redis
4. ✅ **Well documented** - Link to GitHub
5. ✅ **Multiple LLM support** - OpenAI or Ollama

---

## 📊 Usage Instructions for Others

When users visit your Docker Hub page, they should be able to:

```bash
# Quick start
docker run -d -p 8000:8000 \
  -e DEMO_MODE=true \
  -e REDIS_HOST=redis \
  aditya26062003/ai-npc-system:latest

# Or with docker-compose
curl -O https://raw.githubusercontent.com/EchoSingh/AI-NPC/main/docker-compose.yml
docker-compose up -d
```

Then visit: http://localhost:8000/docs
