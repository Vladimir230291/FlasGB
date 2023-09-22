import random
from typing import Annotated
import uvicorn
from fastapi import FastAPI, HTTPException, Request, Form
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates(directory="templates")
users = []


class UserAdd(BaseModel):
    name: str
    email: str
    password: str


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


for i in range(1, 11):
    users.append(User(id=i,
                      name=f"User {i}",
                      email=f"user{i}@example.com",
                      password=str(random.randint(1000, 9999))))


# Вывод всех пользователей
@app.get("/", response_class=HTMLResponse)
async def all_users(request: Request):
    print(users)
    return template.TemplateResponse("all_user.html", {"request": request, "users": users})


@app.post("/add_user", response_model=list[User])
async def add_user(new_user: UserAdd):
    users.append(User(id=len(users) + 1,
                      name=new_user.name,
                      email=new_user.email,
                      password=new_user.password))
    return users


@app.put("/update_user/{id}", response_model=User)
async def update_user(id: int, new_user: UserAdd):
    try:
        current_user = users[id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user:
        current_user.name = new_user.name
        current_user.email = new_user.email
        current_user.password = new_user.password
        return users[id - 1]


@app.delete("/delete_user/{id}", response_model=dict)
async def delete_user(id: int):
    try:
        users.pop(id - 1)
    except IndexError:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}


@app.get("/new_user/", response_class=HTMLResponse)
async def new_user(request: Request):
    return template.TemplateResponse('add_user.html', {'request': request})


@app.post("/new_user/", response_class=HTMLResponse)
async def create_user(request: Request,
                      name: Annotated[str, Form()],
                      email: Annotated[str, Form()],
                      password: Annotated[str, Form()]):
    users.append(User(id=len(users) + 1, name=name, email=email, password=password))
    return template.TemplateResponse('all_user.html', {'request': request, 'users': users})


if __name__ == "__main__":
    uvicorn.run("Home_work5.main:app", host="127.0.0.1", port=8000, reload=True)
