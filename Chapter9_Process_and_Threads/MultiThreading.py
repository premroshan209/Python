# Multi-Threading
# ~~~~~~~~~~~~~~~~
# It is a kind of asynchronous programming. But the main difference is about workers and tasks. 
# Mutil-Threading is about workers and asyncrounous programming is about tasks. 

# If we get a clone to like the pictures on instagram while you wait in line then that is an example of multithreading. 
# Thus you can say you have two workers. You and your clone. While asynchronous programming is about tasks. 
# While waiting for the waiting in line for movie task to finish you can like instagram pictures. 
# There is no other clone or a another human being to complete the other task.

# But what if instead of a clone another different human bring came to like your pictures while you waiting in the line. 
# Then that is an example of multi-Processing. You must have heard of dual-core or multi-core laptops in the old days.
# Now almost every computer has a multi-core. So these core inside your CPU can actually execute the tasks 
# in parellel which is also knowns as parellel programming or multi-processing.

import multiprocessing

print(multiprocessing.cpu_count())

 