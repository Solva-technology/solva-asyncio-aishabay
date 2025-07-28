import asyncio


async def safe_divide(a, b):
    await asyncio.sleep(0.1)
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка деления"


async def run_divisions():
    pairs = [(5, 1), (3, 0), (4, 2)]
    tasks = [safe_divide(a, b) for a, b in pairs]
    return await asyncio.gather(*tasks)
