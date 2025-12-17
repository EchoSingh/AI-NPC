# Quick Start Guide

## 🚀 Running the Project

### 1. Setup Environment
```bash
cd /home/asrathore/Downloads/NPC

# Create .env file
cp .env.example .env

# Edit and add your OpenAI API key
nano .env
# Change: OPENAI_API_KEY=your_openai_api_key_here
```

### 2. Start with Docker Compose
```bash
# Build and start all services
docker-compose up --build -d

# View logs
docker-compose logs -f

# Check status
docker-compose ps
```

### 3. Test the API
```bash
# Health check
curl http://localhost:8000

# View API docs
# Open in browser: http://localhost:8000/docs
```

### 4. Create Example NPCs
```bash
# Wait 10 seconds for services to start, then:
./create_examples.sh
```

### 5. Test Chat
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "player_id": "test_player",
    "npc_id": "blacksmith_thorin",
    "message": "Hello! Can you help me?"
  }'
```

---

## 📦 Push to GitHub

### First Time Setup
```bash
cd /home/asrathore/Downloads/NPC

# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: AI NPC System with personality, memory, and quest generation"

# Create repository on GitHub (via web or CLI)
# Then add remote and push:
git remote add origin https://github.com/EchoSingh/NPC.git
git branch -M main
git push -u origin main
```

### Using GitHub CLI (gh)
```bash
# Login to GitHub
gh auth login

# Create repository and push
gh repo create NPC --public --source=. --remote=origin --push

# Or if repo exists:
git remote add origin https://github.com/EchoSingh/NPC.git
git push -u origin main
```

### Update Repository
```bash
# After making changes:
git add .
git commit -m "Your commit message"
git push
```

---

## 🐳 Push to Docker Hub

### 1. Login to Docker Hub
```bash
docker login
# Username: aditya26062003
# Password: [your Docker Hub password]
```

### 2. Build and Tag Image
```bash
cd /home/asrathore/Downloads/NPC

# Build the image
docker build -t aditya26062003/ai-npc-system:latest .

# Tag with version
docker tag aditya26062003/ai-npc-system:latest aditya26062003/ai-npc-system:1.0.0
```

### 3. Push to Docker Hub
```bash
# Push latest
docker push aditya26062003/ai-npc-system:latest

# Push version tag
docker push aditya26062003/ai-npc-system:1.0.0
```

### 4. Verify
Visit: https://hub.docker.com/r/aditya26062003/ai-npc-system

### 5. Others Can Use It
```bash
# Pull and run your image
docker pull aditya26062003/ai-npc-system:latest
docker run -p 8000:8000 --env-file .env aditya26062003/ai-npc-system:latest
```

---

## 🔄 Complete Workflow

```bash
# 1. Run locally and test
docker-compose up --build -d
docker-compose logs -f

# 2. Commit to Git
git add .
git commit -m "Add feature X"

# 3. Push to GitHub
git push origin main

# 4. Build Docker image
docker build -t aditya26062003/ai-npc-system:latest .

# 5. Push to Docker Hub
docker push aditya26062003/ai-npc-system:latest

# 6. Update README with Docker Hub link
# Add to README: docker pull aditya26062003/ai-npc-system:latest
```

---

## 📝 Update README on Docker Hub

After pushing, update your Docker Hub repository:

1. Go to https://hub.docker.com/r/aditya26062003/ai-npc-system
2. Click "Edit" → "Description"
3. Add this:

```markdown
# AI NPC System for RPG Games 🎮

Intelligent NPCs with personality, memory, and dynamic quest generation.

## Quick Start

```bash
# Pull the image
docker pull aditya26062003/ai-npc-system:latest

# Create .env file
cat > .env << EOF
OPENAI_API_KEY=your_key_here
REDIS_HOST=redis
REDIS_PORT=6379
EOF

# Run with docker-compose
curl -O https://raw.githubusercontent.com/EchoSingh/NPC/main/docker-compose.yml
docker-compose up -d
```

## Features
- 🧠 Intelligent conversations via LLM
- 🎭 6 personality types
- 💾 Persistent memory with Redis
- 🗺️ Dynamic quest generation
- 🐳 Production ready

## Documentation
https://github.com/EchoSingh/NPC
```

---

## 🎯 Quick Commands Cheat Sheet

```bash
# Start project
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop project
docker-compose down

# Rebuild
docker-compose up --build

# Push to GitHub
git add . && git commit -m "Update" && git push

# Push to Docker Hub
docker build -t aditya26062003/ai-npc-system:latest . && docker push aditya26062003/ai-npc-system:latest

# Clean Docker
docker system prune -a
```

---

## 🐛 Troubleshooting

### Port already in use
```bash
# Check what's using port 8000
lsof -i :8000

# Use different port in docker-compose.yml
# Change: "8001:8000"
```

### Docker Hub push denied
```bash
# Logout and login again
docker logout
docker login
```

### Redis connection failed
```bash
# Restart Redis
docker-compose restart redis

# Check Redis logs
docker-compose logs redis
```

---

## 📊 GitHub Repository Checklist

- [x] README.md with badges and screenshots
- [x] LICENSE file (MIT)
- [x] .gitignore for Python/Docker
- [x] Docker support (Dockerfile + docker-compose.yml)
- [x] API documentation (API.md)
- [x] Examples (EXAMPLES.md)
- [x] Contributing guide (CONTRIBUTING.md)
- [ ] Add GitHub Actions for CI/CD
- [ ] Add screenshots/demo GIFs
- [ ] Star your own repo!

---

## 🌟 Make it Trending

1. **Add topics** on GitHub:
   - `ai`, `npc`, `rpg`, `game-development`, `fastapi`, `llm`, `openai`, `redis`, `docker`

2. **Create demo video/GIF**:
   ```bash
   # Record terminal with asciinema
   asciinema rec demo.cast
   # Convert to GIF with agg
   ```

3. **Write a blog post** about it

4. **Share on**:
   - Reddit: r/gamedev, r/programming, r/Python
   - Twitter/X with hashtags: #gamedev #AI #IndieGame
   - Dev.to / Hashnode

5. **Add to README**:
   - Demo GIF
   - Live demo link (deploy on Railway/Render)
   - Video walkthrough
