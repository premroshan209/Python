
# Synchronous
# ~~~~~~~~~~~~
# In sequence. One after other. Thread is blocked.Speed of execution of code depends on your process.
# Has to wait for the funtion to end ( Example infinite while loop)

# Asynchronous
# ~~~~~~~~~~~~
# Doesn't has to wait for a part of code to be finished before executing another one.

# Example
# Human (thread) is waiting in line for movie tickets. For the sake of this example , 
# he is unique human being who can only do 1 thing at a time. So while waiting in line for movie tickets. 
# He can't do anything else. We can also say he has locked on to only getting movie tickets. 
# He can't use intagram while getting movie tickets. Only after he has gotten the movie tickets 
# he can start using instagram on his phone. This is an example of synchronous programming. 
# Now this sounds a lil dumb he should be a ble to use instagram which waiting in line for the movie tickets. 
# This in code is achived by asynchronous programming.


# Aim - To get movie tickets and like instagram pictures

# Synchronous
# We first get the movie tickets and then open the instagram app and like pictures
import time

start = time.time()
def get_movie_tickets() :
    time.sleep(7)
    print("Got the movie tickets")

def like_ig_pic() :
    time.sleep(3)
    print("finshed instagram")

def main():
    get_movie_tickets()
    like_ig_pic()

main()
end = time.time()

print("the time of execution(sync..):", (end - start))

# Asynchronous
# If while waiting in line we use instagram and when the queue has ended then we get our movie tickets

import asyncio

start2 = time.time()
async def get_movie_tickets2() :
    await asyncio.sleep(7)
    print("Got the movie tickets")

async def like_ig_pic2() :
    await asyncio.sleep(3)
    print("finshed instagram")

async def main2():
    task1 = asyncio.create_task(get_movie_tickets2())  # create task to run parallaly 
    task2 = asyncio.create_task(like_ig_pic2())
    await task1  # wait for finish task 1
    await task2  # wait for finish task 2

asyncio.run(main2())
end2 = time.time()

print("the time of execution (Async..):", (end2 - start2))

# Co-routines - Any function that has the async keyword written before it.

