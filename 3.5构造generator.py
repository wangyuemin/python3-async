class async_generator:
    def __init__(self, stop):
        self.i = 0
        self.stop = stop

    async def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        self.i += 1
        if self.i <= self.stop:
            await asyncio.sleep(1)
            return i * i
        else:
            raise StopAsyncIteration


async def main():
    async for i in async_generator(3):
        print(i)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
