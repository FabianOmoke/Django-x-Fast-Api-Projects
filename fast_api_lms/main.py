from fastapi import FastAPI, Path, Query
from pydantic import BaseModel
from typing import Optional,List
from api import users, courses, sections


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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)