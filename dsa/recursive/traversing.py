

"""
If i equals n , we have reached (or passed) the end of the array, so we simply return -end the recursion
"""

def printme(arr,i,n):
    if n == i:
        return

    print(arr[i])
    return printme(arr, i+1, n)
n = int(input())
arr = list(map(int,input().split(" ")))
printme(arr,0,n)









