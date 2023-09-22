from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="lesson5_fastapi/templates")


# HTML "ответ"
@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<h1>Hello World!</h1>"


# JSON "ответ"
@app.get("/message")
async def read_message():
    message = {"message": "Hello World!"}
    return JSONResponse(content=message, status_code=200)


# Ответ страницей html из шаблона с применением Jinja
@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str):
    print(request)  # alternative to log
    return templates.TemplateResponse("item.html", {"request": request, "name": name})
