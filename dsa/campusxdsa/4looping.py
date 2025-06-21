
n= 100
k = 0
l = n//2

for v in range(l,n,2):

    v += 4
    m= 4

    for p in range(m,n): # m is not changing
        #print(j,'j')


        k = k + n // 2
        #print(k,'k')
        print(p,m,n,"p " "m" "n")
        p += 5




def range_with_doubling_step(start, stop):
    current = start
    step = 1
    while current < stop:
        yield current
        current += step
        step *= 2

for i in range_with_doubling_step(1, 100):
    print(i, end=" ")
# Output: 1 2 4 8 16 32 64


def range_with_doubling_steps(start, stop):
    i = start
    step = 1
    while i < stop:
        yield i
        i += step
        step *= 2

for num in range_with_doubling_step(1, 100):
    print(num, end=" ")
# Output: 1 2 4 8 16 32 64



for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)

start = 1
stop = 100
step = 1

i = start
while i < stop:
    print(i)
    i += step
    step *= 2

# recursive tc = how many func call= in factorial it is linear
# in fac(5) 5 time called in fac(10) `10 times  so exponential
# in fibonacci it is exponential 2**n












