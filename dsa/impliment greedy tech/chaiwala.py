
def solve(a):
    count = 0
    time = 0
    for i in range(len(a)):
        if a[i] < time:
            continue
        count += 1
        time += a[i]
    return count
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split(" ")))
    a.sort()
    print(a)
    print(solve(a))












"""
3
3 3 1
"""