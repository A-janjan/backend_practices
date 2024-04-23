from pydantic import BaseModel, EmailStr
from typing import ClassVar


class User(BaseModel):
    email: EmailStr
    password: str

    class Config:
        schema_extra: ClassVar[dict] = {
            "example": {
                "email": "fastapi@packt.com",
                "password": "strong!!!",
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