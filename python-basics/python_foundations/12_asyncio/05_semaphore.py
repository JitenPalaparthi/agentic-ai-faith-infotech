import asyncio

sem = asyncio.Semaphore(2)

async def worker(i):
    async with sem:
        print("start", i)
        await asyncio.sleep(0.1)
        print("end", i)

async def main():
    await asyncio.gather(*(worker(i) for i in range(5)))

asyncio.run(main())
