from typing import Optional
from fastapi import APIRouter, Depends
from apis import chat

from chatbot.character import Character
from chatbot.summary import Summary

from pydantic import BaseModel
from typing import Optional

import requests
import zipfile

class ChatSchema(BaseModel):
    chat: str
    
class ChatListSchema(BaseModel):
    chatList: list

router = APIRouter(
    prefix="/api", # url 앞에 고정적으로 붙는 경로추가
) # Route 분리
    
@router.post("/chat/{id}")
async def chatting(id: int, chat_input: ChatSchema):
    character = Character(id)
    response = character.receive_chat(chat_input.chat)
    
    return { "data": response }

@router.post("/chat/summary/{id}")
async def summary(id: int, chat_input: ChatListSchema):
    summary = Summary(chat_input.chatList, id)
    data = summary.summary()
    
    # endpoint = 'http://3.37.233.51:5001/genimage'
    # response = requests.post(endpoint, json=data)
    
    # if response.status_code == 200:
    #     with open('images.zip', 'wb') as file:
    #         file.write(response.content)
    # else:
    #     print("Failed to retrieve the image. Status code:", response.status_code)
        
    # with zipfile.ZipFile('routes/images.zip', 'r') as zip_ref:
    #     zip_ref.extractall('routes/images')
    
    return { "data": data }