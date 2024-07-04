from fastapi import FastAPI

path_parameters = FastAPI()


@path_parameters.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@path_parameters.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
