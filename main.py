from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
templates = Jinja2Templates(
    directory=os.path.join(BASE_DIR, "templates"))

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home_view(request: Request):
    return templates.TemplateResponse("home.html", {'request': request})


# @app.post("/")
# async def home_detail_view(request: Request):
#     return {'hello': 'world'}
