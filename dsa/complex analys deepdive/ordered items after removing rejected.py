tc = int(input())
for i in range(tc):
    n = int(input())
    items = list(map(int,input().split(" ")))
    m = int(input())
    not_liked =  list(map(int,input().split(" ")))
    liked = []
    for j in range(n):
        if items[j] not in not_liked:
            liked.append(items[j])
    print(liked)
    for ele in liked:
        print(ele,end=" ")
    print()













