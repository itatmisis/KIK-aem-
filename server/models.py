from pydantic import BaseModel


class AuthorizationResult(BaseModel):
    is_ok: bool = False
    error: str = ""
    is_super: bool = False
    is_admin: bool = False

class User(BaseModel):
    email: str = ''
    login: str
    password: str
    is_superuser: bool = False
    is_admin: bool = False


