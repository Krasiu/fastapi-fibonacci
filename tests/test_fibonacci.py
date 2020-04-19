import asyncio
from collections.abc import AsyncGenerator

from app.fibonacci import fibonacci, fibonacci_first_n


def test_fibonacci_returns_async_generator():
    fib = fibonacci()
    assert isinstance(fib, AsyncGenerator)


def test_fibonacci_first_n_returns_list():
    fib = asyncio.run(fibonacci_first_n(5, sleep_for=0.001))
    assert isinstance(fib, list)


def test_fibonacci_1_equals_0():
    fib = asyncio.run(fibonacci_first_n(10, sleep_for=0.001))
    assert fib[0] == 0


def test_fibonacci_2_equals_1():
    fib = asyncio.run(fibonacci_first_n(10, sleep_for=0.001))
    assert fib[1] == 1


def test_fibonacci_10_equals_55():
    fib = asyncio.run(fibonacci_first_n(10, sleep_for=0.001))
    assert fib[9] == 55


def test_fibonacci_first_n_10_is_subsequence_of_fibonacci_first_n_20():
    fib_first_n_10 = asyncio.run(fibonacci_first_n(10, sleep_for=0.001))
    fib_first_n_20 = asyncio.run(fibonacci_first_n(20, sleep_for=0.001))
    assert fib_first_n_10 == fib_first_n_20[:10]
