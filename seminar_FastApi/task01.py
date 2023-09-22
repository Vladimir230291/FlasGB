from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str


class TaskIn(BaseModel):
    title: str
    description: Optional[str]
    status: str


@app.get("/tasks/", response_model=list[Task])
async def root():
    return tasks


@app.post("/tasks/", response_model=list[Task])
async def create_task(new_task: TaskIn):
    tasks.append(
        Task(
            id=len(tasks) + 1,
            title=new_task.title,
            description=new_task.description,
            status=new_task.status,
        )
    )
    return tasks


@app.put("/tasks/", response_model=Task)
async def edit_task(id: int, new_task: TaskIn):
    try:
        current_task = tasks[id - 1]
    except IndexError as e:
        raise HTTPException(status_code=404, detail="Task not found")
    if current_task:
        current_task.title = new_task.title
        current_task.description = new_task.description
        current_task.status = new_task.status
    else:
        return HTTPException(status_code=404, detail="Task not found")
    return tasks[id - 1]


@app.delete("/tasks/", response_model=dict)
async def delete_task(id: int):
    try:
        tasks.pop(id - 1)

    except IndexError as e:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
