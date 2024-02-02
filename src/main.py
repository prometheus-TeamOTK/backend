import os
from typing import Optional
from fastapi import FastAPI
from routes.chat import router as chat_router

from starlette.middleware.cors import CORSMiddleware

app = FastAPI() # FastAPI 모듈
app.include_router(chat_router) # 다른 route파일들을 불러와 포함시킴

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/") # Route Path
def index():
    return {
        "Python": "Framework",
    }
