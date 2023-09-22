from fastapi import FastAPI
import logging
from typing import Optional
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# Создание некого объекта на основе базовой модели
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/")
async def index():
    logger.info("Отработал GeT запрос")
    return {"Hello": "World!"}


@app.post("/items/")
async def read_item(item: Item):
    logger.info("Отработал POST запрос")
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    logger.info(f"Отработал PUT запрос for item_id: {item_id}")
    return {"item_id": item_id, "item": item}


@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    logger.info(f"Отработал DELETE запрос for item_id: {item_id}")
    return {"item_id": item_id}
