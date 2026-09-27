import asyncio

async def hello():
    await asyncio.sleep(0.1)
    return "hello"

print(asyncio.run(hello()))
