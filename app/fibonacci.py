import asyncio


async def fibonacci(sleep_for: float = 1):
    a, b = 0, 1
    await asyncio.sleep(sleep_for)
    yield a

    while True:
        a, b = b, a + b
        await asyncio.sleep(sleep_for)
        yield b


async def fibonacci_first_n(n: int, sleep_for: float = 1):
    sequence = []
    async for number in fibonacci(sleep_for):
        sequence.append(number)
        if len(sequence) == n:
            return sequence
