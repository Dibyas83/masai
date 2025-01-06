n=5
arr = [2,3,4,5,6,7,8,]
target = 9
flag = True
for i in range(n-1):
    for j in range (i+1,n):
        if arr[i] + arr[j] == target:
            print(i,j)
            break
        flag = False
if flag:
    print(-1,-1)


 c =1
 m =1
for i in range(n-1):
    if arr[i]< arr[i+1]:
        c+=1
    else:
        c =1
    if m<c:
        m=c
print(m)




