from fastapi import FastAPI, Depends

import uvicorn

from database import database, metadata, engine
from config import settings
from security import create_access_token

# Import models so metadata contains tables
import models.account  # noqa: F401
import models.transactions  # noqa: F401

from controllers import account as account_controller
from controllers import transactions as transactions_controller
from schemas.auth import AuthIn, TokenOut


app = FastAPI(title="Desafio API Bancária")


@app.on_event("startup")
async def startup():
    # create tables if they don't exist
    metadata.create_all(engine)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(account_controller.router)
app.include_router(transactions_controller.router)


@app.post("/auth/login", response_model=TokenOut)
async def login(data: AuthIn):
    # For the challenge purpose: any user_id is accepted and returns a token
    token = create_access_token(str(data.user_id))
    return TokenOut(access_token=token)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
