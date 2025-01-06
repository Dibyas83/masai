
def re_arrange(N ,arr):

    arr = list(map(int, input().strip().split(" ")))
    N = len(arr)
    for i in range(N):
        if arr[i] == 0:
            arr.remove(0)
            arr.append(0)
        else:
            continue
    print(arr)
N=9
arr = [3,-4,0,5,7,8,1,0,2]
re_arrange(N,arr)

def re_arrange(N ,arr):
    for i in range(N):
        if arr[i] == 0:
            arr.remove(0)
            arr.append(0)
        else:
            continue
    # print(" ".join(map(str,arr)))
    print(arr)
N=9
arr = [3,-4,0,5,7,8,1,0,2]
re_arrange(N,arr)


def re_arrange(N, arr):
    for i in range(N):
        if arr[i] == 0:

            arr.remove(0)
            arr.append(0)
        else:
            continue
    print(" ".join(map(str,arr)))

N = 8
arr = [45,0,-2,0,1,-4,0,7]
re_arrange(N,arr)

























