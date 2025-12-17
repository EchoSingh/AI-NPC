#!/bin/bash

# AI NPC System - Quick Setup Script

echo "🎮 AI NPC System - Quick Setup"
echo "================================"

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "Visit: https://docs.docker.com/get-docker/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker found"
echo "✅ Docker Compose found"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your OpenAI API key:"
    echo "   nano .env"
    echo ""
    read -p "Press Enter after you've added your API key..."
fi

# Build and start services
echo ""
echo "🚀 Building and starting services..."
docker-compose up --build -d

# Wait for services to be ready
echo ""
echo "⏳ Waiting for services to start..."
sleep 5

# Check if API is responding
echo ""
echo "🔍 Checking API health..."
if curl -s http://localhost:8000 > /dev/null; then
    echo "✅ API is running!"
else
    echo "❌ API is not responding. Check logs with: docker-compose logs"
    exit 1
fi

# Display info
echo ""
echo "================================================"
echo "🎉 AI NPC System is ready!"
echo "================================================"
echo ""
echo "📡 API Endpoint: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
echo "📖 ReDoc: http://localhost:8000/redoc"
echo ""
echo "📋 Quick Commands:"
echo "  View logs: docker-compose logs -f"
echo "  Stop: docker-compose down"
echo "  Restart: docker-compose restart"
echo ""
echo "🧪 Test the API:"
echo "  curl http://localhost:8000"
echo ""
echo "Happy coding! 🚀"
