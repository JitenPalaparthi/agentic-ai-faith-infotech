import asyncio, httpx

async def main():
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/get", timeout=5)
        print(r.status_code)

asyncio.run(main())
