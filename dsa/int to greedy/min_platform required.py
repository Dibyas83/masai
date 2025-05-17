

x = int(input()) # no of trains
arr  = list(map(str,input().split(" ")))  # 09:00
dep  = list(map(str,input().split(" ")))
plt = 0   # platforms
list1 = []
for i in range(x):
    ha,ma = arr[i].split(":") # hr,min of arr
    hd,md = dep[i].split(":")
    ta = int(ha)*60 + int(ma)
    td = int(hd)*60 + int(md)
    list1.append(td) # again appended new td due to loopl
    print(list1)
    print(ta) # ta changes due to loop
    if min(list1) > ta:
        plt += 1
    else:
        p = min(list1)
        list1.remove(p) # curr min is removed
print(plt)








