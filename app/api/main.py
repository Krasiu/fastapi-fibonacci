from uuid import UUID

from celery.result import AsyncResult
from fastapi import FastAPI

from app.tasks.celery import app as celery_app

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello": "Fibonacci"}


@app.get("/fibonacci/{n}", status_code=202)
async def get_first_n_fibonacci_numbers(n: int):
    result: AsyncResult = celery_app.send_task(name="app.celery.generate_first_n_fibonacci_numbers", args=[n])
    return {"task_id": result.id, "@uri": f"/tasks/{result.id}"}


@app.get("/tasks/{uuid}")
async def get_task(uuid: UUID):
    result: AsyncResult = AsyncResult(str(uuid), app=celery_app)
    return {"task_id": result.id, "status": result.status, "result": result.result}
