from typing import Optional
from fastapi import APIRouter, Depends
from apis import chat

from chatbot.character import Character

router = APIRouter(
    prefix="/api", # url 앞에 고정적으로 붙는 경로추가
) # Route 분리
    
@router.get("/chat")
async def chatting():
    response = await chat.get_response()
    return response