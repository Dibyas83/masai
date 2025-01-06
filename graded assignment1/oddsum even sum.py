"""
sum at odd and even positions
"""
sum1 =0
sum2 =0
arr = [0,1,22,3,4,5,6,7,8,9,11,12,13,14]
N = len(arr)
for i in arr[0:N+1:2]:
    sum1 += i

for i in arr[1:N+1:2]:
    sum2 += i

if sum1 > sum2:
    print("even")
if sum1<sum2:
    print("odd")

# not at position
























