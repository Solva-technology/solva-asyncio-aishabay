import aiohttp
import asyncio


async def fetch_status(session, url):
    async with session.get(url) as response:
        return response.status


async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        statuses = []
        for url in urls:
            statuses.append(await fetch_status(session, url))
    return statuses


async def main():
    print(await fetch_all(["https://httpbin.org/status/200"]))


if __name__ == "__main__":
    asyncio.run(main())
