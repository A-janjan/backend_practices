from pydantic import BaseModel, EmailStr
from typing import ClassVar, Optional, List
from beanie import Document, Link
from models.events import Event


class User(BaseModel):
    email: EmailStr
    password: str
    events: Optional[List[Link[Event]]]

    class Settings:
        name = "users"

    class Config:
        schema_extra: ClassVar[dict] = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    schema_extra: ClassVar[dict] = {
        "example": {
            "email": "fastapi@packt.com",
            "password": "strong!!!"
        }
    }
