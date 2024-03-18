from fastapi import FastAPI, Form, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import webbrowser
from fastapi.templating import Jinja2Templates
import subprocess

app = FastAPI()

# middlewares
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_credentials=True, allow_methods=['*'],allow_headers=['*'])

# Set up Jinja2 templates
templates = Jinja2Templates(directory="D:\\Mohamed\\FCIS\\4th\\GP\\VITON\\ModyVITON\\web\\frontend")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index2.html', {"request": request})


@app.post("/getIds")
async def handle_numbers(num1: int = Form(...), num2: int = Form(...)):
    # Your endpoint logic here
    result = num1 + num2
    print(result)


@app.get("/page2", response_class=HTMLResponse)
async def read_page2(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


def run_virtual_tryon_app():
    port = 80
    ngrok_tunnel = ngrok.connect(port)

    # where we can visit our fastAPI app
    tryon_url = ngrok_tunnel.public_url
    print('Public URL for Tryon Application:', tryon_url)
    webbrowser.open(tryon_url)

    nest_asyncio.apply()

    # finally run the app
    uvicorn.run(app, host="0.0.0.0", port=port)


run_virtual_tryon_app()
