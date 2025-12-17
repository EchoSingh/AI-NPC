# AI NPC System for RPG/Open World Games 🎮🤖

![GitHub](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.0-green)
![Docker](https://img.shields.io/badge/docker-ready-blue)
![Docker Pulls](https://img.shields.io/docker/pulls/aditya26062003/ai-npc-system)
![Docker Image Size](https://img.shields.io/docker/image-size/aditya26062003/ai-npc-system)

> **Create intelligent, memorable NPCs with personality, memory, and dynamic quest generation powered by LLMs**

An advanced AI-powered NPC system that brings RPG characters to life with intelligent dialogue, persistent memory, distinct personalities, and dynamic quest generation. Built with FastAPI, Redis, and LLM integration (OpenAI/Ollama).

## ✨ Features

### 🧠 **Intelligent Conversations**
- Natural language processing via OpenAI GPT or local Ollama models
- Context-aware responses based on conversation history
- NPCs remember previous interactions with players

### 🎭 **Rich Personalities**
- **6 Distinct Personality Types:**
  - 😊 **Friendly** - Warm, helpful, and enthusiastic
  - 😠 **Aggressive** - Hostile and confrontational
  - 🔮 **Mysterious** - Cryptic and enigmatic
  - 💰 **Merchant** - Business-minded and persuasive
  - 🧙 **Wise** - Knowledgeable and mentor-like
  - 😂 **Comedic** - Humorous and witty

### 💾 **Persistent Memory System**
- Redis-powered memory storage
- Conversation history tracking (last 50 messages)
- Player reputation system (-100 to +100)
- NPC statistics and interaction counts

### 🗺️ **Dynamic Quest Generation**
- AI-generated quests tailored to NPC personality
- Customizable difficulty levels
- Context-aware quest creation
- Structured quest objectives and rewards

### 🐳 **Production Ready**
- Docker containerization
- Docker Compose for easy deployment
- Scalable architecture
- RESTful API design

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- OpenAI API key (or Ollama for local LLM)

### 1️⃣ Clone and Setup

```bash
git clone https://github.com/EchoSingh/NPC.git
cd NPC

# Create environment file
cp .env.example .env

# Add your OpenAI API key to .env
nano .env
```

### 2️⃣ Configure Environment

Edit `.env` file:

```env
# For OpenAI (Cloud)
OPENAI_API_KEY=your_openai_key_here
OPENAI_MODEL=gpt-3.5-turbo

# For Ollama (Local) - Alternative
USE_OLLAMA=false
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2
```

### 3️⃣ Launch with Docker

**Option A: Using Docker Compose (Recommended)**
```bash
# Build and start services
docker-compose up --build -d

# View logs
docker-compose logs -f
```

**Option B: Using Pre-built Docker Image**
```bash
# Pull from Docker Hub
docker pull aditya26062003/ai-npc-system:latest

# Run with docker-compose
docker-compose up -d
```

The API will be available at: **http://localhost:8000**

### 4️⃣ Verify Installation

```bash
curl http://localhost:8000
```

Expected response:
```json
{
  "status": "online",
  "message": "AI NPC System is running",
  "version": "1.0.0"
}
```

---

## 📖 Documentation

### Interactive API Docs
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Documentation Files
- **[API Reference](docs/API.md)** - Complete API documentation
- **[Examples & Usage](docs/EXAMPLES.md)** - Ready-to-use NPC examples
- **[Contributing Guide](docs/CONTRIBUTING.md)** - How to contribute

### Core Endpoints

#### 🆕 Create NPC
```bash
POST /npc
```

**Example Request:**
```json
{
  "npc_id": "blacksmith_01",
  "name": "Thorin Ironforge",
  "personality": "friendly",
  "background": "A master blacksmith who has crafted weapons for heroes across the realm. Loves sharing stories of legendary battles.",
  "location": "Town Forge"
}
```

**Response:**
```json
{
  "npc_id": "blacksmith_01",
  "name": "Thorin Ironforge",
  "personality": "friendly",
  "background": "A master blacksmith...",
  "location": "Town Forge",
  "conversation_count": 0
}
```

#### 💬 Chat with NPC
```bash
POST /chat
```

**Example Request:**
```json
{
  "player_id": "player_123",
  "npc_id": "blacksmith_01",
  "message": "Hello! Can you repair my sword?"
}
```

**Response:**
```json
{
  "npc_response": "Ah, greetings friend! Of course I can repair your sword! Let me take a look at it. I've been smithing for over 30 years, and I haven't seen a blade I couldn't fix yet!",
  "npc_emotion": "friendly",
  "quest_offered": false
}
```

#### 🗺️ Generate Quest
```bash
POST /quest/generate
```

**Example Request:**
```json
{
  "player_id": "player_123",
  "npc_id": "blacksmith_01",
  "context": "Player needs a legendary weapon"
}
```

**Response:**
```json
{
  "quest_id": "a7b3c9d1-e4f5-6789-g0h1-i2j3k4l5m6n7",
  "title": "The Lost Mithril Ore",
  "description": "Deep in the Shadowmount Mines lies a vein of pure mithril ore. Bring it back and I'll forge you a weapon of legend.",
  "difficulty": "hard",
  "reward": "Legendary Weapon + 500 Gold",
  "objectives": [
    "Travel to Shadowmount Mines",
    "Defeat the mine guardians",
    "Extract pure mithril ore",
    "Return to Thorin Ironforge"
  ]
}
```

#### 📊 Check Reputation
```bash
GET /reputation/{player_id}/{npc_id}
```

**Response:**
```json
{
  "player_id": "player_123",
  "npc_id": "blacksmith_01",
  "reputation": 15,
  "level": "Friendly"
}
```

#### 📜 View Conversation History
```bash
GET /history/{player_id}/{npc_id}?limit=10
```

---

## 🏗️ Architecture

```
┌─────────────────┐
│   Game Client   │
└────────┬────────┘
         │ HTTP/REST
         ▼
┌─────────────────┐
│  FastAPI Server │
│   (Port 8000)   │
└────┬───────┬────┘
     │       │
     │       └──────────────┐
     ▼                      ▼
┌──────────┐        ┌──────────────┐
│  Redis   │        │ LLM Service  │
│ (Memory) │        │ OpenAI/Ollama│
└──────────┘        └──────────────┘
```

### Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **API Server** | FastAPI | RESTful endpoints, request handling |
| **Memory Store** | Redis | Persistent NPC memory & conversations |
| **LLM Engine** | OpenAI/Ollama | Natural language generation |
| **Personality Engine** | Python | Character trait management |
| **Quest Generator** | LLM-powered | Dynamic quest creation |

---

## 🎮 Usage Examples

### Example 1: Merchant NPC

```bash
# Create merchant
curl -X POST http://localhost:8000/npc \
  -H "Content-Type: application/json" \
  -d '{
    "npc_id": "merchant_01",
    "name": "Sly Pete",
    "personality": "merchant",
    "background": "A cunning trader who always has rare items... for the right price.",
    "location": "Market Square"
  }'

# Chat with merchant
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "player_id": "player_456",
    "npc_id": "merchant_01",
    "message": "What rare items do you have?"
  }'
```

### Example 2: Aggressive Guard

```bash
# Create guard
curl -X POST http://localhost:8000/npc \
  -H "Content-Type: application/json" \
  -d '{
    "npc_id": "guard_01",
    "name": "Captain Brutus",
    "personality": "aggressive",
    "background": "A battle-hardened guard who doesn'\''t tolerate nonsense.",
    "location": "City Gates"
  }'
```

### Example 3: Wise Wizard

```bash
# Create wizard
curl -X POST http://localhost:8000/npc \
  -H "Content-Type: application/json" \
  -d '{
    "npc_id": "wizard_01",
    "name": "Eldrin the Ancient",
    "personality": "wise",
    "background": "An ancient wizard with centuries of magical knowledge.",
    "location": "Tower of Mysteries"
  }'

# Generate quest from wizard
curl -X POST http://localhost:8000/quest/generate \
  -H "Content-Type: application/json" \
  -d '{
    "player_id": "player_789",
    "npc_id": "wizard_01",
    "context": "Player seeks magical training"
  }'
```

---

## � Project Structure

```
NPC/
├── app/                    # Application source code
│   ├── main.py             # FastAPI routes & endpoints
│   ├── models.py           # Pydantic data models
│   ├── memory.py           # Redis memory manager
│   ├── personality.py      # NPC personality engine
│   ├── llm_service.py      # LLM integration
│   └── config.py           # Configuration management
├── docs/                   # Documentation
│   ├── API.md              # Complete API reference
│   ├── EXAMPLES.md         # Usage examples
│   └── CONTRIBUTING.md     # Contribution guidelines
├── scripts/                # Helper scripts
│   ├── create_examples.sh  # Create sample NPCs
│   └── setup.sh            # Quick setup script
├── docker-compose.yml      # Docker orchestration
├── Dockerfile              # Container image
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## �🛠️ Development

### Local Setup (Without Docker)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Start Redis (separate terminal)
redis-server

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run development server
python -m app.main
# or
uvicorn app.main:app --reload
```

### Using Ollama (Local LLM)

```bash
# Install Ollama
curl https://ollama.ai/install.sh | sh

# Pull a model
ollama pull llama2

# Update .env
USE_OLLAMA=true
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# Run the application
docker-compose up
```

### Project Structure

```
NPC/
├── app/
│   ├── main.py              # FastAPI application & routes
│   ├── config.py            # Configuration management
│   ├── models.py            # Pydantic models
│   ├── memory.py            # Redis memory manager
│   ├── personality.py       # Personality engine
│   └── llm_service.py       # LLM integration
├── docker-compose.yml       # Docker orchestration
├── Dockerfile               # Container image
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
└── README.md               # Documentation
```

---

## 🎨 Personality Types Guide

### 😊 Friendly
- **Best for**: Shopkeepers, innkeepers, helpful villagers
- **Traits**: Warm, enthusiastic, helpful
- **Example NPC**: Friendly tavern owner, village healer

### 😠 Aggressive
- **Best for**: Guards, bandits, rival warriors
- **Traits**: Hostile, confrontational, intimidating
- **Example NPC**: Gate guard, enemy faction leader

### 🔮 Mysterious
- **Best for**: Prophets, fortune tellers, shadowy figures
- **Traits**: Cryptic, enigmatic, philosophical
- **Example NPC**: Oracle, mysterious stranger

### 💰 Merchant
- **Best for**: Traders, shop owners, negotiators
- **Traits**: Business-minded, persuasive, opportunistic
- **Example NPC**: Traveling merchant, auction house owner

### 🧙 Wise
- **Best for**: Mentors, scholars, elders
- **Traits**: Knowledgeable, patient, thoughtful
- **Example NPC**: Master wizard, village elder

### 😂 Comedic
- **Best for**: Jesters, comic relief characters
- **Traits**: Humorous, witty, playful
- **Example NPC**: Town jester, quirky inventor

---

## 📊 Memory System

### Conversation Storage
- **Duration**: 7 days
- **Capacity**: Last 50 messages per player-NPC pair
- **Format**: Timestamped with context

### Reputation System
- **Range**: -100 (Enemy) to +100 (Trusted Ally)
- **Levels**:
  - 51-100: Trusted Ally
  - 1-50: Friendly
  - 0: Neutral
  - -1 to -50: Disliked
  - -51 to -100: Enemy

### Reputation Factors
- Polite language: +2 per positive keyword
- Rude language: -3 per negative keyword
- Personality modifiers applied
- Impacts NPC responses and quest availability

---

## 🔧 Configuration Options

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key | - |
| `OPENAI_MODEL` | OpenAI model name | gpt-3.5-turbo |
| `USE_OLLAMA` | Use Ollama instead of OpenAI | false |
| `OLLAMA_BASE_URL` | Ollama server URL | http://localhost:11434 |
| `OLLAMA_MODEL` | Ollama model name | llama2 |
| `REDIS_HOST` | Redis hostname | redis |
| `REDIS_PORT` | Redis port | 6379 |
| `API_HOST` | API server host | 0.0.0.0 |
| `API_PORT` | API server port | 8000 |

---

## 🐳 Docker Hub

**Pull the image:**
```bash
docker pull aditya26062003/ai-npc-system:latest
```

**View on Docker Hub:** https://hub.docker.com/r/aditya26062003/ai-npc-system

**Available tags:**
- `latest` - Most recent build
- `1.0.0` - Stable release

## 🐳 Docker Commands

```bash
# Build and start
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes (clears Redis data)
docker-compose down -v

# Restart specific service
docker-compose restart api
```

---

## 📸 Screenshots & Demo

### API Documentation (Swagger UI)
Visit http://localhost:8000/docs for interactive API testing

### Example Interactions

**Friendly Blacksmith:**
```
Player: "Hello! I need a new sword."
NPC: "Ah, welcome friend! You've come to the right place! I have the finest blades in all the kingdom. What kind of sword are you looking for?"
```

**Aggressive Guard:**
```
Player: "Can I pass through the gate?"
NPC: "Halt! State your business quickly, and it better be legitimate. I don't have time for troublemakers."
```

**Mysterious Oracle:**
```
Player: "What do you see in my future?"
NPC: "The threads of fate are tangled around you... darkness approaches, yet within it lies opportunity. Will you be ready when the moment comes?"
```

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Powered by [OpenAI](https://openai.com/) / [Ollama](https://ollama.ai/)
- Memory by [Redis](https://redis.io/)

---

## 📧 Contact

**GitHub**: [@EchoSingh](https://github.com/EchoSingh)
**Docker Hub**: [aditya26062003](https://hub.docker.com/u/aditya26062003)

---

## 🎯 Roadmap

- [ ] Voice synthesis integration
- [ ] Multi-language support
- [ ] NPC-to-NPC conversations
- [ ] Advanced quest chains
- [ ] Emotion detection in player messages
- [ ] WebSocket support for real-time chat
- [ ] Unity/Unreal Engine integration examples

---

## ⚡ Performance Tips

1. **Use Redis persistence** for production
2. **Enable OpenAI streaming** for faster responses
3. **Implement rate limiting** for API endpoints
4. **Use connection pooling** for Redis
5. **Cache frequently accessed NPCs** in memory

---

## 🐛 Troubleshooting

### Redis Connection Error
```bash
# Check Redis is running
docker-compose ps

# Restart Redis
docker-compose restart redis
```

### OpenAI API Error
```bash
# Verify API key in .env
cat .env | grep OPENAI_API_KEY

# Test API key
curl https://api.openai.com/v1/models \
  -H "Authorization: Bearer $OPENAI_API_KEY"
```

### Docker Build Issues
```bash
# Clean rebuild
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

---

<div align="center">

### ⭐ Star this repo if you find it useful!

**Made with ❤️ for game developers**

</div>
