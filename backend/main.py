from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    userInput: str


@app.get("/", response_class=HTMLResponse)
def main():
    with open("../frontend/index.html") as f:
        mainpage = f.read()
    return mainpage


class Model:
    def __init__(self):
        self.data = "thinh"

    def predict(self, inputString):
        return inputString + self.data


model = Model()


@app.post("/codeflow")
def read_item(item: Item):
    return model.predict(item.userInput)
