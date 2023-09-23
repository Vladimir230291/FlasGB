from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name: str = Field(..., title="Name", max_length=50, min_length=2)
    price: float = Field(..., title="Price", gt=0, le=100_000)
    description: str = Field(default=None, title="Description", max_length=100)
    tax: float = Field(0, title="Tax", ge=0, le=10)


@app.post("/items/")
async def create_item(item: Item):
    return {"item": item}