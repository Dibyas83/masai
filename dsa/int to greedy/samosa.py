

n,k = map(int,input().split(" ")) # n shops with one samosa each
l = sorted(list(map(int,input().split()))) # cost on each shop
num = k
count = 0
for i in l:
    if i <= num:
        count += 1
        num -= i
print(count)

"""
4 10
5 4 2 4
"""










