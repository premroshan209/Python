
# use predefind libraries for file handling 
# 1. aiofiles
# 2. aiohttp

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Synchronous : 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import time

s = time.time()

def fetch_file():
    print("Start Featching File..")
    time.sleep(1)
    print("End Featching File.")

def main():
    print("main started for sync..")
    fetch_file()
    fetch_file()
    fetch_file()

main()

e = time.time()

print("Total file featching time (sync..) :",(e - s))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Asynchronous:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import asyncio

start = time.time()

async def fetch_file2():
    print("Fetch Started..")
    await asyncio.sleep(1)
    print("Fetch end.")

async def main2():
    print("Started Main function for Async..")
    # task1 = asyncio.create_task(fetch_file2())
    # task2 = asyncio.create_task(fetch_file2())
    # task3 = asyncio.create_task(fetch_file2())

    # await task1
    # await task2
    # await task3

    await asyncio.gather(
        fetch_file2(),
        fetch_file2(),
        fetch_file2()
        )

asyncio.run(main2())

end = time.time()
print("Total file featching time (Async..) :",(end - start))