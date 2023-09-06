from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pymysql
from pydantic import BaseModel

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/popup.html")
async def popup(request: Request):
    return  templates.TemplateResponse("popup.html",{"request":request})

@app.get("/signup/req-in")
async def signup():
    return {"signup":"up"}

""" @app.post("/mypage/{user_id}")
async def read_user(
    user_id: Player.id,
) """