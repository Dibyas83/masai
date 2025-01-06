q = int(input("enter no and query type= "))
results = []
X =0
for _ in range(q):
    query= input().split()
    query_type = int(query[0])


    if query_type == 1:

        X = int(query[1]) * 2
    elif query_type == 2:
        X = int(query[1]) * 3
    elif query_type == 3:
        X = int(query[1]) +10
    elif query_type == 4:
        X = int(query[1]) + 25
        print(X)
    elif query_type == 5:
        results.append(-1)
        print(X)
    if query_type!= 5:
        results.append(X)

for result in results:
    print(results)