from pydantic import BaseModel

from typing import List, Optional

class AuthorizationResult(BaseModel):
    is_ok: bool = False
    error: str = ""

class User(BaseModel):
    email: str
    password: str
    is_superuser: bool = False
    is_admin: bool = False

class SuperUser(User):
    is_superuser: bool = True
    is_admin: bool = False

class Admin(SuperUser):
    is_admin: bool = True

class Position(BaseModel):
    direction: str
    date: str
    country: str
    product_code: str
    unit: int               #Единица измерения
    cost: int
    weght: float
    quantity: int
