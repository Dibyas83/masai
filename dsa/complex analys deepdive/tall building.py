
# 0 if smaller than left and right, 1 if > l or r,2 if > l and r
n = int(input())
score = 0
list1 = list(map(int,input().split(" ")))
for i in range(n):
    if i == 0:
        if list1[i] > list1[i+1]:
            score += 1
            print(1, end=" ")
        else:
            print(0, end=" ")
    elif i == n-1:
        if list1[i] > list1[i-1]:
            score += 1
            print(1, end=" ")
        else:
            print(0,end=" ")
    else:
        if list1[i] > list1[i - 1] and list1[i] > list1[i+1]:
            score += 2
            print(2, end=" ")
        elif list1[i] > list1[i - 1] or list1[i] > list1[i + 1]:
            score += 1
            print(1, end=" ")
        else:
            print(0, end=" ")
print()
print(score)










