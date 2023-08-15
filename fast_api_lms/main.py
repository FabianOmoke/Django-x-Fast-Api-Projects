from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional,List


app = FastAPI(
    title="Fast API LMS",
    description='LMS for managing Students and Courses',
    version= "0.1" ,  #version of the api
    contact = {
        'name': 'Fabian Ombui',
        'email': "omoke8116@gmail.com"   
    },
    license_info={
        'name':'MIT',
        },
)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

@app.get("/users", response_model =List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "User Added"}

@app.get("/users/{id}")
async def get_user(
    # path variables before query parameters
    id: int = Path(..., description =" ID of user we we'd like to retrive", gt=2),
    q: str = Query(None, max_length=5)
    ):
    return {"user": users[id], "query": q }