from typing import Optional, List

from fastapi import FastAPI, Query
from pydantic import BaseModel

task_api = FastAPI()


class Task(BaseModel):
    title: str
    content: str
    is_actual: Optional[bool] = None


@task_api.get("/")
async def read_root():
    return {"Hello": "World"}


@task_api.get("/tasks/get_by_id/{task_id}")
async def get_task_by_id(task_id: int, q: Optional[str] = None):
    return {"task_id": task_id, "q": q}


@task_api.get("/tasks/get_by_title/")
async def get_task_by_title(
        task_title: str = Query(
            ...,
            alias="task-title",
            title="Task title",
            description="Task title to search in the database that have a good match",
            min_length=5,
            max_length=50
        )
):
    return {"task_title": task_title}


@task_api.get("/tasks/get_list/")
async def get_task_by_title(task_titles: List[str] = Query(...)):
    return {"task_titles": task_titles}


@task_api.put("/tasks/update/{task_id}")
async def update_task(task_id: int, task: Task):
    return {"task_name": task.title, "task_id": task_id}


@task_api.post("/tasks/add")
async def add_task(task_id: int):
    return task_id


@task_api.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
