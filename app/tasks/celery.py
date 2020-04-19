import asyncio

from celery import Celery

from app.fibonacci import fibonacci_first_n

app = Celery(
    'tasks',
    backend="db+sqlite:///celery.sqlite",
    broker="pyamqp://user:bitnami@rabbitmq//"
)


@app.task(name="app.celery.generate_first_n_fibonacci_numbers")
def generate_first_n_fibonacci_numbers(n: int):
    first_n_fibonacci_numbers = asyncio.run(fibonacci_first_n(n=n))
    return first_n_fibonacci_numbers
