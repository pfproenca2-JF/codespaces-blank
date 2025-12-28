from pydantic import BaseModel


class AuthIn(BaseModel):
    user_id: int


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"
