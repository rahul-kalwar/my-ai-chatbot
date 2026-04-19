import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from groq import Groq
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

conversations = {}

async def generate_response(message: str, session_id: str = "default"):
    try:
        if session_id not in conversations:
            conversations[session_id] = []
        
        conversations[session_id].append({"role": "user", "content": message})
        
        stream = client.chat.completions.create(
           model="llama-3.1-8b-instant",
            messages=conversations[session_id],
            temperature=0.7,
            stream=True
        )
        
        full_response = ""
        for chunk in stream:
            if chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                full_response += content
                safe_content = content.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')
                yield f'data: {{"type": "content", "content": "{safe_content}"}}\n\n'
        
        conversations[session_id].append({"role": "assistant", "content": full_response})
        
    except Exception as e:
        error_msg = str(e).replace('\\', '\\\\').replace('"', '\\"')
        yield f'data: {{"type": "error", "content": "{error_msg}"}}\n\n'
    
    yield f'data: {{"type": "end"}}\n\n'

@app.get("/")
async def root():
    return {"message": "AI Chatbot Backend is Running"}

@app.get("/chat_stream/{message}")
async def chat_stream(message: str, session_id: str = "default"):
    return StreamingResponse(generate_response(message, session_id), media_type="text/event-stream")