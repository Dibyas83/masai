
n= int(input().strip())
arr1 = list(map(int,input().split(" ")))
def count_inversion(arr,left,mid,right):
    n1 = mid -left + 1
    n2 =right-mid
    l= arr[left:mid + 1]
    r = arr[mid+1:right+1]

    i = 0
    j = 0
    k = left
    cnt1 = 0
    while i < n1 and j < n2: # merge in descending order
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
            cnt1 += (n1-i) # how many left ele are greater than right
        print(cnt1)
        k += 1
        print(arr,"progress")

    while i < n1:
        arr[k] = l[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = r[j]
        j += 1
        k += 1
    return cnt1

def cnt1(arr,left,right):
    c = 0 # count
    if left < right:

        mid = (left + right) // 2
        c += cnt1(arr,left,mid)

        c += cnt1(arr,mid+1,right)

        c += count_inversion(arr,left,mid,right)
    return c

res = cnt1(arr1,0,n-1)
print(res)












