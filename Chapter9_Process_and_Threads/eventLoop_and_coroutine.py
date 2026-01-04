# Aim -
# 1) Create our own event loop
# 2) Create a co-routine
# 3) Execute that co-routine using our own event loop


# Coroutine: a pause-able function
# Event Loop: the scheduler that runs coroutines efficiently

# await :
# 1) Used to pause a co-routine so that another co-routine can get executed to completion
# 2) Await should always be inside a co-routine


import asyncio

# Example 1 :

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

print(loop)  #loop is an object 

async def task1() :
    print("Task 1 Started...")
    await asyncio.sleep(2)
    print("Task 1 End")

async def task2() :
    print("Task 2 Started...")
    await asyncio.sleep(1)
    print("Task 2 End")

# run multiple coroutines using gather
loop.run_until_complete(asyncio.gather(task1(), task2()))

loop.close()




# Example 2:

async def square(num):
    return num * num

async def main() :
    x = await square(5)     #there is await so main coroutine function pause here and run the square coroutine function, once square is completed it come back to main
    print(x)

    y = await square(10)
    print(y)

    z = await square(15)
    print(z)

    sum = x + y + z
    print("Sum =",sum)

asyncio.run(main())