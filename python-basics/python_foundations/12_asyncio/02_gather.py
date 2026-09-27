import asyncio

async def work(n):
    await asyncio.sleep(0.1)
    return n*n

async def main():
    print(await asyncio.gather(*(work(i) for i in range(5))))

asyncio.run(main())
