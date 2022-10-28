from typing import List, Optional

from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str
    moderator: bool = False


class AuthorizationResult(BaseModel):
    is_ok: bool = False
    error: str = ""


class Search(BaseModel):
    text: str = ""
    is_moscow: bool = False
    category: int = -1
