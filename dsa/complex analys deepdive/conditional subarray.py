# arr = 1,2,3,4  sub = 1 12 123 1234  2 23 234 3 34.count the no of subarrays having that no
N,K = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
cnt = 0
for i in range(N):
    sub_array = []
    for j in range(i,N):
        sub_array.append(arr[j])
        print(sub_array)
        even_count = 0
        for el in sub_array:
            if el%2 == 0:
                even_count += 1 # no of even nos
        if even_count == K: # if sub array has k even nos
            cnt += 1
            print("count = ",cnt)
print(cnt)

"""
5 2
2 4 5 7 8
[2]
[2, 4]
count =  1
[2, 4, 5]
count =  2
[2, 4, 5, 7]
count =  3
[2, 4, 5, 7, 8]
[4]
[4, 5]
[4, 5, 7]
[4, 5, 7, 8]
count =  4
[5]
[5, 7]
[5, 7, 8]
[7]
[7, 8]
[8]
4
"""






