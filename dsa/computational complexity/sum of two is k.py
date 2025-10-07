
"""
perm = n(n-1)(n-r+1)  r nos
comb = c * r! =  p     r at a time=n!/r!*(n-r)!
"""
no_pl = int(input())

wanted_sum =  int(input())
sorted_arr = list(map(int,input().split(" ")))
"""
for i in range(no_pl):
    sorted_arr[i] = int(input())

g = len(sorted_arr)
for i in range(no_pl):


    #print(sorted_arr[i], sorted_arr[len-1])
    if sorted_arr[i] + sorted_arr[g-1] == wanted_sum:
        print(sorted_arr[i], sorted_arr[g-1])
        break
    elif sorted_arr[i] + sorted_arr[g-1] > wanted_sum:
        g  = g-1
    elif sorted_arr[i] + sorted_arr[g-1] < wanted_sum:
        if i < 6:
            i = i+1

"""

left,right = 0,len(sorted_arr) -1
flag = 0
while left < right:
    curr_sum = sorted_arr[left] + sorted_arr[right]

    if curr_sum == wanted_sum:
        flag = 1
        print(sorted_arr[left], sorted_arr[right])
        break
    elif curr_sum < wanted_sum:
        left += 1
    else:
        right -= 1










