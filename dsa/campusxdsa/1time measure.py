import time

start = time.time()
for i in range(1,100):
    print(i)
print(time.time() - start)

start1 = time.time()
j= 1
while j < 100:
    print(j)
    j += 1
print(time.time() - start1)
