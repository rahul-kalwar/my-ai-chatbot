# AI Chatbot - My AI Chat Buddy

## Project Description

AI-powered chatbot that allows users to have natural conversations with real-time streaming responses. The chatbot maintains conversation memory, remembering what you told it earlier in the same session.

**In plain language:** You type a question or tell the bot something about yourself, and it responds instantly. It remembers your name and what you talked about during your conversation.

## Architecture Overview

The application follows a client-server architecture with separate frontend and backend services:
┌─────────────────┐ HTTP/SSE ┌─────────────────┐ API Call ┌─────────────────┐
│ │ ◄──────────────► │ │ ◄──────────────► │ │
│ React Frontend │ │ FastAPI Backend│ │ Groq API │
│ (Port 3000) │ │ (Port 8000) │ │ (Llama/Mixtral)│
│ │ │ │ │ │
└─────────────────┘ └─────────────────┘ └─────────────────┘

## Technical Choices
- **React/Next.js**: Modern UI framework
- **FastAPI**: Async support for streaming responses
- **Groq API**: Free tier, no credit card required, 30+ requests/min
- **SSE**: Real-time response streaming

## Setup Instructions

### Prerequisites
Python 3.10+, Node.js 18+, Git

### Steps
```bash
# Clone and setup backend
git clone <your-repo-url>
cd perplexity_2.0/server
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Add API key to .env file
echo GROQ_API_KEY=your-key-here > .env

# Start backend
uvicorn app:app --reload

# New terminal - setup frontend
cd ../client
npm install
npm run dev
Open http://localhost:3000

Known Limitations
Free tier rate limits (30 req/min)

No persistent storage (conversations lost on refresh)

No user authentication

Single-user design

Production Changes Needed
Add database (PostgreSQL)

Add user authentication (JWT)

Replace uvicorn with gunicorn + nginx

Enable HTTPS

AI Tools Used
Claude AI: Debugging, error fixes, migration from Gemini to Groq

GitHub Copilot: Code completion

Demo Video
[Link]

Team
[Your Name] - [Student ID]

Level
Level 2 - Multi-turn conversation with memory


