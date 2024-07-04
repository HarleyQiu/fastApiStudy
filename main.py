from fastapi import FastAPI
from pydantic import BaseModel, validator
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    model_messages = {
        ModelName.alexnet: "Deep Learning FTW!",
        ModelName.lenet: "LeCNN all the images",
        ModelName.resnet: "Have some residuals"
    }
    message = model_messages.get(model_name, "Model not recognized")
    return {"model_name": model_name, "message": message}
