
# Processes are isolated and canot share memory with other processes
# A process can have 1 thread or multiple threads that share the systems resources.

import threading

def infiniteLoop():
    print("Infinite Loop Started..")
    while 1 == 1:
        pass

def printmsg():
    print("Hello Prem")

t1 = threading.Thread(target=infiniteLoop)
t2 = threading.Thread(target=printmsg)

t1.start()
t2.start()