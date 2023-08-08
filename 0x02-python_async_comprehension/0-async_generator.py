#!/usr/bin/env python3
'''
The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
Use the random module.
'''


import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''async generator'''
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.random() * 10
