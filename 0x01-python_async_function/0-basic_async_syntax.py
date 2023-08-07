#!/usr/bin/env python3
'''
asynchronous coroutine that takes in an int argument
(max_delay, default = 10) named wait_random
that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it.
'''


import asyncio
import random


async def wait_random(max_delay=10):
    '''The basics of async'''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
