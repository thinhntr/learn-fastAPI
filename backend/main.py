from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    userInput: str


@app.get("/")
def read_root():
    return {"name": "LearnFastAPI"}


class Model:
    def __init__(self):
        self.data = "thinh"

    def predict(self, inputString):
        return inputString + self.data


model = Model()


@app.post("/codeflow")
def read_item(item: Item):
    return model.predict(item.userInput)
