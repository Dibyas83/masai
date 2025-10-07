
n = int(input())
arr1 = list(map(int,input().split(" ")))
n1 =  n//2
for j in range(n):
    if(arr1.count(arr1[j]) > n1):
        print(arr1[j])
        break
    else:
        print("-1")
        break







