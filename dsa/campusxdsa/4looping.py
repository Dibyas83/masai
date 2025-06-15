
n= 10
k = 0
m = 2
for i in range(n//2,n):
    print(i,'i')
    for j in range(m,n):
        print(j,'j')
        k = k + n // 2
        print(k,'k')
        m = m*2

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


def range_with_doubling_step(start, stop):
    i = start
    step = 1
    while i < stop:
        yield i
        i += step
        step *= 2

for num in range_with_doubling_step(1, 100):
    print(num, end=" ")
# Output: 1 2 4 8 16 32 64







