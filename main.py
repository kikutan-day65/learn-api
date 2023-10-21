from fastapi import FastAPI
from fastapi.params import Body


app = FastAPI()


# GET request
@app.get("/")
def root():
    return {"message": "Welcome to my API"}


@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}


# POST request
@app.post("/createposts")
def create_posts(payLoad: dict = Body(...)): # data stored in payLoad
    print(payLoad)
    return {"new_post": f"title: {payLoad['title']} content: {payLoad['content']}"}