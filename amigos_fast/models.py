from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

class Gender(str, Enum):
    MALE = "male" # male gender
    FEMALE = "Female"# female gender

class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id: Optional[UUID] = uuid4
    first_name: str
    last_name:  str
    middle_name: Optional[str]
    gender: Gender
    roles : list[Role]


