# API Reference

Complete API documentation for the AI NPC System.

## Base URL

```
http://localhost:8000
```

---

## Authentication

Currently, no authentication is required. For production, implement API keys or OAuth2.

---

## Endpoints

### Root

#### Health Check
```http
GET /
```

**Response:**
```json
{
  "status": "online",
  "message": "AI NPC System is running",
  "version": "1.0.0"
}
```

---

## NPC Management

### Create NPC

Create a new NPC with personality and background.

```http
POST /npc
```

**Request Body:**
```json
{
  "npc_id": "string",
  "name": "string",
  "personality": "friendly|aggressive|mysterious|merchant|wise|comedic",
  "background": "string",
  "location": "string"
}
```

**Response:** `201 Created`
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

**Errors:**
- `400 Bad Request` - NPC already exists
- `500 Internal Server Error` - Storage failure

---

### Get NPC

Retrieve NPC details by ID.

```http
GET /npc/{npc_id}
```

**Path Parameters:**
- `npc_id` (string, required) - Unique NPC identifier

**Response:** `200 OK`
```json
{
  "npc_id": "blacksmith_01",
  "name": "Thorin Ironforge",
  "personality": "friendly",
  "background": "A master blacksmith...",
  "location": "Town Forge",
  "conversation_count": 5
}
```

**Errors:**
- `404 Not Found` - NPC doesn't exist

---

### Delete NPC

Delete an NPC and all associated data.

```http
DELETE /npc/{npc_id}
```

**Path Parameters:**
- `npc_id` (string, required) - Unique NPC identifier

**Response:** `200 OK`
```json
{
  "message": "NPC 'blacksmith_01' deleted successfully"
}
```

**Errors:**
- `404 Not Found` - NPC doesn't exist
- `500 Internal Server Error` - Deletion failure

---

## Interaction

### Chat with NPC

Send a message to an NPC and receive a response.

```http
POST /chat
```

**Request Body:**
```json
{
  "player_id": "string",
  "npc_id": "string",
  "message": "string"
}
```

**Example:**
```json
{
  "player_id": "player_123",
  "npc_id": "blacksmith_01",
  "message": "Can you repair my sword?"
}
```

**Response:** `200 OK`
```json
{
  "npc_response": "Of course, friend! Let me take a look at that blade...",
  "npc_emotion": "friendly",
  "quest_offered": false
}
```

**Errors:**
- `404 Not Found` - NPC doesn't exist

**Side Effects:**
- Updates conversation history
- Modifies player reputation
- Increments conversation count

---

### Get Conversation History

Retrieve past conversations between a player and NPC.

```http
GET /history/{player_id}/{npc_id}?limit=20
```

**Path Parameters:**
- `player_id` (string, required) - Player identifier
- `npc_id` (string, required) - NPC identifier

**Query Parameters:**
- `limit` (integer, optional) - Max messages to retrieve (default: 20)

**Response:** `200 OK`
```json
[
  {
    "timestamp": "2025-12-18T10:30:00",
    "player_message": "Hello!",
    "npc_response": "Greetings, friend!",
    "context": {
      "reputation": "5"
    }
  }
]
```

---

### Get Reputation

Check player's reputation with an NPC.

```http
GET /reputation/{player_id}/{npc_id}
```

**Path Parameters:**
- `player_id` (string, required) - Player identifier
- `npc_id` (string, required) - NPC identifier

**Response:** `200 OK`
```json
{
  "player_id": "player_123",
  "npc_id": "blacksmith_01",
  "reputation": 15,
  "level": "Friendly"
}
```

**Reputation Levels:**
- `51-100`: Trusted Ally
- `1-50`: Friendly
- `0`: Neutral
- `-1 to -50`: Disliked
- `-51 to -100`: Enemy

---

## Quests

### Generate Quest

Request an AI-generated quest from an NPC.

```http
POST /quest/generate
```

**Request Body:**
```json
{
  "player_id": "string",
  "npc_id": "string",
  "context": "string (optional)"
}
```

**Example:**
```json
{
  "player_id": "player_123",
  "npc_id": "blacksmith_01",
  "context": "Player needs a legendary weapon"
}
```

**Response:** `200 OK`
```json
{
  "quest_id": "a7b3c9d1-e4f5-6789",
  "title": "The Lost Mithril Ore",
  "description": "Retrieve pure mithril from the Shadowmount Mines",
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

**Errors:**
- `404 Not Found` - NPC doesn't exist

---

## Data Models

### PersonalityType (Enum)

```typescript
enum PersonalityType {
  FRIENDLY = "friendly",
  AGGRESSIVE = "aggressive",
  MYSTERIOUS = "mysterious",
  MERCHANT = "merchant",
  WISE = "wise",
  COMEDIC = "comedic"
}
```

### NPCCreate

```typescript
{
  npc_id: string;           // Required
  name: string;             // Required
  personality: PersonalityType; // Required
  background: string;       // Required
  location?: string;        // Optional, default: "Unknown"
}
```

### NPCResponse

```typescript
{
  npc_id: string;
  name: string;
  personality: PersonalityType;
  background: string;
  location: string;
  conversation_count: number;
}
```

### Message

```typescript
{
  player_id: string;    // Required
  npc_id: string;       // Required
  message: string;      // Required
}
```

### ChatResponse

```typescript
{
  npc_response: string;
  npc_emotion?: string;
  quest_offered: boolean;
}
```

### Quest

```typescript
{
  quest_id: string;
  title: string;
  description: string;
  difficulty: string;   // "easy" | "medium" | "hard"
  reward: string;
  objectives: string[];
}
```

---

## Error Responses

All error responses follow this format:

```json
{
  "detail": "Error message describing what went wrong"
}
```

### Common HTTP Status Codes

- `200 OK` - Successful request
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid request data
- `404 Not Found` - Resource doesn't exist
- `500 Internal Server Error` - Server-side error

---

## Rate Limiting

Currently no rate limiting is implemented. For production:
- Implement per-IP rate limiting
- Consider per-user rate limiting
- Add retry-after headers

---

## Webhooks (Future)

Planned webhook support for:
- NPC state changes
- Quest completion
- Reputation milestones

---

## WebSocket API (Future)

Planned WebSocket endpoint for real-time chat:

```
ws://localhost:8000/ws/{player_id}/{npc_id}
```

---

## Examples

### Python

```python
import requests

# Create NPC
response = requests.post(
    "http://localhost:8000/npc",
    json={
        "npc_id": "wizard_01",
        "name": "Gandalf",
        "personality": "wise",
        "background": "A powerful wizard",
        "location": "Tower"
    }
)
print(response.json())

# Chat with NPC
response = requests.post(
    "http://localhost:8000/chat",
    json={
        "player_id": "player_1",
        "npc_id": "wizard_01",
        "message": "I seek your wisdom"
    }
)
print(response.json()["npc_response"])
```

### JavaScript

```javascript
// Create NPC
const createNPC = async () => {
  const response = await fetch('http://localhost:8000/npc', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      npc_id: 'wizard_01',
      name: 'Gandalf',
      personality: 'wise',
      background: 'A powerful wizard',
      location: 'Tower'
    })
  });
  return await response.json();
};

// Chat with NPC
const chat = async () => {
  const response = await fetch('http://localhost:8000/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      player_id: 'player_1',
      npc_id: 'wizard_01',
      message: 'I seek your wisdom'
    })
  });
  const data = await response.json();
  console.log(data.npc_response);
};
```

### cURL

```bash
# Create NPC
curl -X POST http://localhost:8000/npc \
  -H "Content-Type: application/json" \
  -d '{
    "npc_id": "wizard_01",
    "name": "Gandalf",
    "personality": "wise",
    "background": "A powerful wizard",
    "location": "Tower"
  }'

# Chat with NPC
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "player_id": "player_1",
    "npc_id": "wizard_01",
    "message": "I seek your wisdom"
  }'
```

---

## Pagination (Future)

For endpoints returning lists, pagination will be implemented:

```http
GET /npcs?page=1&limit=20
```

---

## Interactive Documentation

Visit the interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
