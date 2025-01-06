t =int(input())
count = 0
for i in range(t):
    n,x= map(int,input().split(" "))  # population and min age
    print(type(n))
    for j in range(n):

        q = list(map(int,input().split()))  # age
        for age in q:
            if age >= x:
                count += 1
        print(count)
    print(q,type(q))
    print(type(n))

