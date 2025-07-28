import asyncio


async def delayed_echo(text, delay):
    await asyncio.sleep(delay)
    return text


async def echo_all():
    tasks = [delayed_echo(item, 1) for item in "hello world !".split()]
    return await asyncio.gather(*tasks)
