

"""
If i equals n , we have reached (or passed) the end of the array, so we simply return -end the recursion
"""


def traverse(arr,i,n):
    if n == i:
        return
    print(arr[i])
    return traverse(arr,i+1,n)

n = int(input())
arr = list(map(int,input().split(" ")))
traverse(arr,0,n)







