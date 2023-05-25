from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class User(BaseModel):
    username: str
    short_description: str
    liked_posts: Optional[list[int]] = None


def get_user_info() -> User:
    content = {
        "username" : 1.54,
        "short_description" : "The bio description",
        "liked_posts" : None
    }

    return User(**content)


@app.get("/user/me", response_model=User)
def test_endpoint():
    user = get_user_info()

    return user

@app.get("/")
def home():
    return "Welcome"


