import asyncio

async def slow():
    await asyncio.sleep(2)

async def main():
    try:
        async with asyncio.timeout(0.1):
            await slow()
    except TimeoutError:
        print("timed out")

asyncio.run(main())
