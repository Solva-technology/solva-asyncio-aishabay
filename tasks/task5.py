import asyncio


async def fast_task():
    await asyncio.sleep(0.1)
    return "fast"


async def medium_task():
    await asyncio.sleep(0.3)
    return "medium"


async def slow_task():
    await asyncio.sleep(1)
    return "slow"


async def first_complete():
    tasks = [
        asyncio.create_task(fast_task()),
        asyncio.create_task(medium_task()),
        asyncio.create_task(slow_task()),
    ]
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    for task in pending:
        task.cancel()

    return next(iter(done)).result()

if __name__ == "__main__":
    first_complete()
