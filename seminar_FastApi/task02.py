from enum import Enum
from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

moves = []


class Genre(Enum):
    ACTION = "Боевик"
    ADVENTURE = "Приключения"
    COMEDY = "Комедия"
    DRAMA = "Драма"
    THRILLER = "Триллер"


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str]
    genre: Genre


@app.get("/movies/", response_model=list[Movie])
async def all_movies():
    return moves


@app.get("/movies/{genre}", response_model=list[Movie])
async def search_genre(genre: Genre):
    try:
        result = [movie for movie in moves if movie.genre == genre]
    except KeyError as e:
        result = HTTPException(status_code=404, detail="Genre not found")
    return result


@app.post("/movies/", response_model=list[Movie])
async def add_movie(new_movie: Movie):
    moves.append(
        Movie(
            id=len(moves) + 1,
            title=new_movie.title,
            description=new_movie.description,
            genre=new_movie.genre,
        )
    )
    return moves


if __name__ == "__main__":
    uvicorn.run("task02:app", host="127.0.0.1", port=8001, reload=True)
