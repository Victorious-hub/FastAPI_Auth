from fastapi import FastAPI
from fastapi import FastAPI, HTTPException, Depends, Request,status

from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.auth import models,router
from database import engine

app = FastAPI()
models.Base.metadata.create_all(bind=engine)
app.include_router(router.router)

origins = [
    "http://localhost:3000",
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    kanban = {
        "task1": {1: "one", 2: "two"},
    }
    return {"message": kanban}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}



if __name__ == '__main__':
    uvicorn.run(f"src.main:app", host="127.0.0.1", port=8000, reload=True)
