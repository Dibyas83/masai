
def solve(k,arrv1,dept):
    ct = 0
    i=0
    j=0
    n=len(arrv1)
    while i < n and j < n:
        if arrv1[i] <= dept[j]:
            i += i # check next car
            ct += 1
        else:
            j += 1 # check if both car goes before third arrives
            ct += 1

        if ct > k:
            return "not possible"

    return "possible"

def inp():
    k = int(input())
    arrv= list(map(int,input().split(" ")))
    dept = list(map(int,input().split(" ")))
    arrv.sort()
    dept.sort()
    print(solve(k,arrv,dept))
inp()










