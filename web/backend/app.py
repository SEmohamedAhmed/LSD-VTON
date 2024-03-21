from fastapi import FastAPI, Form, Request
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import webbrowser
from fastapi.templating import Jinja2Templates
import subprocess
from tryon import *

app = FastAPI()

# middlewares
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'],
                   allow_headers=['*'])

# Set up Jinja2 templates
templates = Jinja2Templates(directory=r"D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\frontend")

# Mount the static files directory
app.mount("/static", StaticFiles(directory=r"D:\Mohamed\FCIS\4th\GP\VITON\VITONY\web\frontend\static"), name="static")


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    return templates.TemplateResponse('Home.html', {"request": request})


class Item(BaseModel):
    choosenAvatarId: str
    chosenGarmentID: str


@app.post("/tryon")
def tryon_model(item: Item):
    # call kaggle API to run our notebook and get its output
    person_id, cloth_id = tryon(item.choosenAvatarId, item.chosenGarmentID)

    # Return the tryon image response as a string of image path relative to static directory
    return f"/static/tryon_results/{person_id}___{cloth_id}.png"


@app.get("/model", response_class=HTMLResponse)
def model(request: Request):
    return templates.TemplateResponse('Model.html', {"request": request})


def start_virtual_tryon_app():
    port = '80'
    ngrok_tunnel = ngrok.connect(port)

    # where we can visit our fastAPI app
    tryon_url = ngrok_tunnel.public_url
    print('Public URL for Tryon Application:', tryon_url)
    webbrowser.open(tryon_url)

    nest_asyncio.apply()
    # finally run the app
    uvicorn.run(app, host="0.0.0.0", port=int(port))


start_virtual_tryon_app()
