from fastapi import FastAPI
from models import User, Gender, Role
from typing import List
from uuid import uuid4

app = FastAPI()

db: List[User] = [
    User(id=uuid4(),first_name="Amigos", last_name="Kijana", middle_name="Wamalwa", gender=Gender.MALE, roles=[Role.admin, Role.student, Role.user])
]

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/")
async def root():
    return {"Hello": "World"}