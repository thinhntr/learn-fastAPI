from typing import Annotated, List

from dataclasses import dataclass

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="views")


@dataclass
class Contact:
    uname: str
    email: str


@dataclass
class Data:
    contacts: List[Contact]

    def hasEmail(self, email):
        for contact in self.contacts:
            if email == contact.email:
                return True
        return False


data = Data(
    [
        Contact("Alice", "alice@gmail.com"),
        Contact("Bob", "bob@gmail.com"),
    ]
)


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    context = {"request": request, "data": data}
    return templates.TemplateResponse(name="index.html", context=context)


@app.post("/contacts")
def create_contact(
    request: Request, uname: Annotated[str, Form()], email: Annotated[str, Form()]
):
    if data.hasEmail(email):
        return templates.TemplateResponse(name="contacts.html", status_code=422)
    data.contacts.append(Contact(uname, email))
    context = {"request": request, "data": data}
    return templates.TemplateResponse(name="contacts.html", context=context)


@app.get("/debug")
def debug():
    return data
