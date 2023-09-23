from typing import List

import databases
import sqlalchemy
from fastapi import FastAPI
from pydantic import Field, BaseModel

DATABASE_URL = "sqlite:///test.db"

databases = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(32)),
    sqlalchemy.Column("email", sqlalchemy.String(128)),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)

app = FastAPI()


class UserIn(BaseModel):
    name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)


class UserOut(BaseModel):
    id: int
    name: str = Field(..., max_length=32)
    email: str = Field(..., max_length=128)


@app.on_event("startup")
async def startup():
    await databases.connect()


@app.on_event("shutdown")
async def shutdown():
    await databases.disconnect()


# Создание фейковых пользователей
# @app.get("/fake_users/{count}")
# async def create_note(count: int):
#     for i in range(count):
#         user = users.insert().values(name=f"user_{i}", email=f"user_{i}@example.com")
#         await databases.execute(user)
#     return {"message": f"Created {count} users"}

# Добавление нового пользователя
@app.post("/users", response_model=UserOut)
async def create_user(user: UserIn):
    query = users.insert().values(name=user.name, email=user.email)
    last_record_id = await databases.execute(query)
    return {**user.dict(), "id": last_record_id}


# Получение всех пользователей
@app.get("/users", response_model=List[UserOut])
async def read_users():
    query = users.select()
    return await databases.fetch_all(query)


# Получение конкретного пользователя
@app.get("/users/{user_id}", response_model=UserOut)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await databases.fetch_one(query)

# Обновление информации о пользователе
@app.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user: UserIn):
    query = users.update().where(users.c.id == user_id).values(name=user.name, email=user.email)
    await databases.execute(query)
    return {**user.dict(), "id": user_id}

# Удаление пользователя
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await databases.execute(query)
    return {"message": "User deleted"}