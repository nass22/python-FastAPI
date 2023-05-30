from pydoc import describe
from fastapi import FastAPI
from fastapi.responses import JSONResponse, PlainTextResponse
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class User(BaseModel):
    username: str = Field(
        title="The Username",
        description="This is the username of the user",
        min_length=1,
        max_length=20,
        default=None
    )
    liked_posts: list[int] = Field(
        description="Array of post ids the user liked",
        min_items=0,
        max_items=10,
        default=None
    )

class FullUserProfile(User):
    short_description: str
    long_bio: str


def get_user_info(user_id: str = "default") -> FullUserProfile:
    profile_infos = {
        "default": {
            "short_description": "The bio description",
            "long_bio": "This is our longer bio"
        },
        "user_1": {
            "short_description": "User 1's bio description",
            "long_bio": "User 1's longer bio"
        },
    }

    profile_info = profile_infos[user_id]

    users_content = {
        "default": {
            "liked_posts": [1] * 9,
            "profile_info": profile_info
        },
        "user_1": {
            "liked_posts": [],
            "profile_info": profile_info
        }      
    }

    user_content = users_content[user_id]
    user = User(**user_content)
    

    full_user_profile = {
        **profile_info,
        **user.dict()
    }
    
    return FullUserProfile(**full_user_profile)


@app.get("/user/me", response_model=FullUserProfile)
def test_endpoint():
    full_user_profile = get_user_info()

    return full_user_profile

@app.get("/user/{user_id}", response_model=FullUserProfile)
def get_user_by_id(user_id: str):
    full_user_profile = get_user_info(user_id)

    return full_user_profile

@app.get("/")
def home():
    return "Welcome"


