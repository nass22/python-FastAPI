from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class ProfileInfo(BaseModel):
    short_description: str
    long_bio: str

class User(BaseModel):
    username: str
    profile_info: ProfileInfo
    liked_posts: Optional[list[int]] = None


def get_user_info() -> User:
    profile_info = {
        "short_description" : "The bio description",
        "long_bio" : "This is our longer bio"
    }
    profile_info = ProfileInfo(**profile_info)

    user_content = {
        "username" : "Username",
        "profile_info" : profile_info,
        "liked_posts" : None
    }

    return User(**user_content)


@app.get("/user/me", response_model=User)
def test_endpoint():
    user = get_user_info()

    return user

@app.get("/")
def home():
    return "Welcome"


