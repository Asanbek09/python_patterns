import asyncio

async def square(x):
    await asyncio.sleep(1)
    return x * x

async def main():
    future1 = asyncio.ensure_future(square(2))
    future2 = asyncio.ensure_future(square(3))
    future3 = asyncio.ensure_future(square(4))

    results = await asyncio.gather(future1, future2, future3)

    for result in results:
        print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())