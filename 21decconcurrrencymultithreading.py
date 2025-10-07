
def chekpos(n):
    if n < 0:
        raise ValueError("Negetive num not allowed!")
    print("less no is ",n)
try:
    n=int(input("input->"))
    chekpos(n)
except ValueError as e:
    print(e)

# no name error acured or error specified
try:
    Print("hi")
    print("hi")
except NameError as e:
    print((e))

def chekpos(n):
    if n < 0:
        raise ValueError("Negetive num not allowed!")
    print("less no is ",n)
try:
    n=int(input("input->"))
    if n < 0:

        raise ValueError("Negetive num not allowed!")
    print("less no is ", n)
except ValueError as e:
    print(e)

num = [1,2,3,4,5]
result = list(map(lambda x:x**2,filter(lambda x:x%2 != 0,num)))
print(result)

# concurrency - divide job and do all small jobs same time, by allocating
# equivalent resources acoding to requirements
# thread is one of co-worker- capacity to divide work according to no of threads
# all threads share same memory ,so coordination is key, one thread process data while anather waits for user input

# 1 Global Intrpretor Lock(GIL) - a safety mechanism that ensures only one thread runs python code at a time if there
# is one coe or thread as resource is shared..when one thread lock is required
# 2 for parallelism we need more threads or core each with own resourse
# lock aquire and then release after process when two thread share same variable - race condition
# lock ensures only one thread acts at a time,a single bathrom key prevents two people from entering
# me withdrawing money by card and online more than balance available- called as race condition
import threading
import time

def cal_ssuare(numd):
    print("calculate sq root")
    for n in numd:
        time.sleep(0.3)# at each iteration it waits for 0.3 sec
        print("square is ",n*n)


arr =[2,3,4,5,6]
ti = time.time()
thread1 = threading.Thread(target=cal_ssuare,args=(arr,))
thread1.start()

# cal_ssuare(arr)
print("total time taken - ",time.time() - ti)
thread1.join()
print("hi")
print("---------------------12")

import threading
import time
def task(name,duration):
    print(f"Task{name} starting...")
    time.sleep(duration) # simulates a task that takes some time
    print(f"Task {name} completed! - Duration : {duration}")

tasks = [("Taski",3),("Task2",2),("task3",1)]
# sequential execution
start_time = time.time()
print("Starting sequential execution ...")
for name,duration in tasks:
    task(name,duration)
end_time = time.time()
seq_time =end_time - start_time
print(f"completed in {seq_time:.2f} sec\n")
# Threading Execution
start_time = time.time()
print("start thread exec")
threads = []
for name,duration in tasks:
    thread = threading.Thread(target=task,args=(name,duration))
    threads.append(thread)
    thread.start()

#wait for all threads to complete
for thread in threads:
    thread.join()

end_time = time.time()
threaded_time = end_time - start_time
print(f"threaded exec completed in{threaded_time:.2f} seconds\n")
print(f'Time saved: {seq_time-threaded_time:.2f} sec')

print("----------------------race condition")

import threading
shsred_counter = 0
# Function to increment the counteer
def incre_counter():
    global shared_counter
    for _ in range(100000):
        shared_counter += 1


# creating threads
threads = []
for _ in range(2):
    thread = threading.Thread(target=incre_counter)
    threads.append(thread)
    thread.start()

#wait for all threads to complete
for thread in threads:
    thread.join()

print(f"final counter value:{shsred_counter}")

print("==================lock")
"""

import threading

shsred_counter1 = 0
lock = threading.Lock()n

def incre_counteer():

"""





# random.seed(x) =  different x values will give different fixed random value




"""
using Thread module
1 - writing a function for task
2 - create a thread using threading.Thread(target=function)
3 - start it with start()
"""
# single thread single task
import threading

def greet(): # task
    print("hello")

t = threading.Thread(target=greet)
t.start() # executing
t.join() # for ending or closing thread

def grrt():
    print("hello")
t = threading.Thread(target=grrt())
t.start()
t.join()

# how to get lock
"""
lock.acquire()
modify shared data
lock.release()
"""
# Ex - 2 thr increment a shared counter 1000 times each.
# fina value could be 2000.
# add a lock around the increment code


shared_counter = 0
def increment1():
    global shared_counter
    for i in range(1000):
        shared_counter += 1


def increment2():
    global shared_counter
    for i in range(1000):
        shared_counter += 1


t1 = threading.Thread(target=increment1)
t2 = threading.Thread(target=increment2)
t1.start()
t2.start()
t1.join()
t2.join()
print(shared_counter)


lock = threading.Lock()

shared_counter2 = 0
def increment11():

    global shared_counter2
    for i in range(1000):
        #lock.acquire()
        shared_counter2 += 1
        #lock.release()


def increment22():

    global shared_counter2
    for i in range(1000):

        #lock.acquire()
        shared_counter2 += 1
        #lock.release()


t11 = threading.Thread(target=increment11)
t22 = threading.Thread(target=increment22)
t11.start()
t22.start()
t11.join()
t22.join()
print(shared_counter2)
print("----------------------675")
#import concurrent.futures as cf
import concurrent.futures as cf
mylist = [1,2,3,4,5,66]

def cube(x):
    return x**3
#with cf.ThreadPoolExecutor() as executor:
with cf.ThreadPoolExecutor() as executor:
    results = list(executor.map(cube,mylist))

print(results)

mylist1 = list(range(10000))
results2 = []

import time
start = time.time()
print(start)

for nums in mylist1:
    results2.append(cube(nums))

stop = time.time()
print(stop-start)

# multitask
start1 = time.time()
with cf.ThreadPoolExecutor(max_workers= 4) as executor:
    results2 = list(executor.map(cube,mylist1))
    # executor.submit(cube, mylist1)

end = time.time()
print(end - start1)


# random4

import random

for i in range(10):
    print(random.randint(1,6))
    print(random.random())

random.seed(10) # 10 is instance name

for i in range(10):
    print(random.randint(1,6))

random.seed(10)
print("-----------------")
for i in range(10):
    print(random.randint(1,6))

# create sting of letters and no,pick 8 letters/no randomly
letnum = "sdss344gdhr54hhdr6345td"

import random
random.seed(15)
seq = ""
for i in range(8):
    seq += random.choice(letnum)
print(seq)



