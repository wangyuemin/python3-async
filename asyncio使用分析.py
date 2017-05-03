import asyncio
from asyncio import Queue


async def first():
    print(100)


async def second():
    for i in range(10):
        print (i)


async def num():
    for i in range(10):
        return i


async def work(myqueue):
    print('lalala')
    while not myqueue.empty():
        i = await myqueue.get()
        print(i)
        myqueue.task_done()


async def third():
    await first()
    myqueue = Queue()
    q = Queue()
    await asyncio.wait([q.put(i) for i in range(10)])
    tasks = [asyncio.ensure_future(work(myqueue))]
    await myqueue.join()
    print (3)
    for task in tasks:
        task.cancel()
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(third())
    loop.close()
