

def lamfuncsort(n,arr,k):
    arr.sort(key = lambda x: x%k)
    print(" ".join(map(str, arr)))

n = int(input())
arr = list(map(int,input().split(" ")))
k = int(input())
lamfuncsort(n,arr,k)

"""
5
4 6 11 22 25
5
25 6 11 22 4
"""


