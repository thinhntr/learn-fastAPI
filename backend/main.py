from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
