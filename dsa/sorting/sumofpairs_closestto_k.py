

def sumpaircloset_k(arr,k):
    arr.sort()
    print(arr)
    left, right = 0, len(arr)-1
    sum = -1 # if no valid pair is found
    m,n = 0,0

    while left<right:
        curr_sum = arr[left] + arr[right]
        if curr_sum < k:
            sum = max(sum,curr_sum)
            m=left
            n=right
            print(sum)
            left+=1
        else:
            right -= 1
    return sum,(arr[m],arr[n])

n= int(input())
arr = list(map(int,input().split(" ")))

print(sumpaircloset_k(arr,11))


"""

7 
4 2 5 6 1 8 4
"""







