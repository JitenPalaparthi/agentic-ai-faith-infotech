import asyncio
async def work(i):
    await asyncio.sleep(0.1)
    return i*i
async def main():
    print(await asyncio.gather(*(work(i) for i in range(5))))
asyncio.run(main())
