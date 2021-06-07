
import aiohttp
import asyncio
import time
import argparse


async def fetch(session, sem, url):
    async with sem:
        await session.get(url)


async def main(threads, file):   
    tasks = []
    sem = asyncio.Semaphore(threads)
    async with aiohttp.ClientSession() as session:
        with open(file) as f:
            for url in f:
                task = asyncio.create_task(fetch(session, sem, url))
                tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=int, default=10)
    parser.add_argument('-f', type=str, default='urls.txt')
    args = parser.parse_args()

    t1 = time.time()
    asyncio.run(main(args.c, args.f))
    t2 = time.time()

    print('Time exceeded: ', t2 - t1)
