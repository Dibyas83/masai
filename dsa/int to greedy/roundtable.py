

from collections import deque
n = int(input())
a = list(map(int,input().split(" ")))
a.sort()
queue = deque([a[0]])
i = 0
ans = float('-inf')
print(queue[-1],"1beg-1") # -1 is last
print(queue[0],"1beg0")
for e in a:
    print(queue[-1], "beg-1")
    print(queue[0], "beg0")
    print(e,"e")
    ans = max(ans, e - queue[0],e - queue[-1])
    print(ans,"loopans")
    if i%2 == 0:
        queue.append(e) # so that max remains away from min no
    else:
        queue.appendleft(e)
    print(queue,e,"queue at e")
    i += 1
print(ans)








