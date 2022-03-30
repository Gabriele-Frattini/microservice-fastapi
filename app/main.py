from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
import pathlib

BASE_DIR = pathlib.Path(__file__).parent

templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates"))

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home_view(request: Request):
    return templates.TemplateResponse("home.html", {'request': request})

