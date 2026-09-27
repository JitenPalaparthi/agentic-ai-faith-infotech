import asyncio

async def work(name):
    await asyncio.sleep(0.1)
    print(name)

async def main():
    tasks = [asyncio.create_task(work(str(i))) for i in range(3)]
    await asyncio.gather(*tasks)

asyncio.run(main())
