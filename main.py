from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True # set True as default if a user doesn't specify the value here
    rating: Optional[int] = None # set None as default  if a user doesn't specify the value here


# GET request
@app.get("/")
def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


# POST request
@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.dict())
    return {"data": post}