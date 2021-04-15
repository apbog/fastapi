from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

task_api = FastAPI()


class Task(BaseModel):
    title: str
    content: str
    is_actual: Optional[bool] = None


@task_api.get("/")
def read_root():
    return {"Hello": "World"}


@task_api.get("/tasks/{task_id}")
def read_task(task_id: int, q: Optional[str] = None):
    return {"task_id": task_id, "q": q}


@task_api.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    return {"task_name": task.title, "task_id": task_id}


@task_api.post("/tasks/add")
def read_task(task_id: int):
    return task_id
