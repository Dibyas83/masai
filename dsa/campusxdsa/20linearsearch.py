"""
1- brute force- one by one


"""
def linear_search(arrr,item):
    for i in range(len(arrr)):
        if arrr[i] == item:
            return i

    return -1
arr12 = [2,4,6,82,44,22,7,11,223]
print(linear_search(arr12,82))
print(linear_search(arr12,3))
print(linear_search(arr12,223))


# binary search- only on sorted data


def binary_search(arr,low,high,item): # index nos

    if low <= high:
        mid = (low + high) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search(arr,low,mid-1,item)
        else:
            return binary_search(arr,mid+1,high,item)

    else:
        return -1

arr = [1,22,35,37,45,48,55,58,59,77,89,91,94,99,222,555,666,777,999]
print(binary_search(arr,0,len(arr),999))
print(binary_search(arr,0,len(arr),94))

# sorting

def is_sorted(arr1):
    sorted = True
    for i in range(len(arr1)-1):
        if arr1[i] > arr1[i+1]:
            sorted = False
    return sorted # will return true

# monkey sort

import random
import time

aa = [1,3,6,8,9,5]
random.shuffle(aa)
print(aa)

def monkey_sort(arr2):

    while not is_sorted(arr2):
        time.sleep(1)
        random.shuffle(arr2)
        print(arr2)
    print(arr2)


aa = [1,3,6,8,9,5]
#monkey_sort(aa)
# tc is infinite

# sleep sort - print the values in array after time equal to value

#------------------------------Bubble short-swap by swap biggest to last,arr size to swap decreases.so no of comparisson is fibonaci= n-1 to 1= !n-1)(n-2)/2= o(n2)

def bobblesort(arr3):
    flag = 0
    for i in range(len(arr3)-1):
        for j in range(len(arr3)-1-i):
            if arr3[j] > arr3[j+1]:
                arr3[j],arr3[j+1] = arr3[j+1],arr3[j]
                flag = 1
        if flag == 0:
            break
    print(arr3)

ar12 = [2,4,6,82,44,22,7,11,223]
bobblesort(ar12)

# adaptive sorting - if it takes advantage of existing order in its input.like binary sort.it understands it has sorted data and its algo is according
# non-adaptive sorting- it checks again-bubble sort even if no swaps ,comparison accurrs.can we make it adaptive.we can have a flag 0 and change to 1 if swapped. even if partialy sorted it will be sorted after some pass.ex 3 2 4 5 6 after onepass its ssorted and in 2nd pass flag=0 and break.so in best case o(n)

#stable - means if we sort strings like Aa,Fi,Hw,Cu,Lo,Ny,Fy,Ug-when sorted fi should come first then fy,ex -bubble short
#unstable ex- heap sort quick short
#-------------------selection short-
def selectionshot(arr4): # i-1 is considered min then comparison accurrs to find min.after the pass swap min with i=0.tc or comparisson = o(n*n) ,1 swaps in each pass so o(n)
    for i in range(len(arr4)-1):
        min = i
        for j in range(i+1,len(arr4)-1):
            if arr4[j] < arr4[min]:
                min = j  # if array is 8,7,8,2,1 after first pass min = 4 and 8 and 1 swaps ,so not stable as 8th pos is interchanged
# after n passes  n items from begining are sorted
        arr4[i],arr4[min] = arr4[min],arr4[i]
    print(arr4)
ar12 = [2,4,6,82,44,22,7,11,223]
selectionshot(ar12)
# space complexity is 1 as we require only var min and changes accurr on original array only.not adaptive as it keeps on comparing for min only 1,4,8,3 there will be no swapping.not stable
li = []
for i in range(100):
    li.append(random.randint(1,100))
print(li[1:40])
l3 = li[1:40]
l2 = li[1:40]

start = time.time()
bobblesort(l3)
print("time taken",time.time() - start,"sec")


start = time.time()
selectionshot(l2)
print("time taken",time.time() - start,"sec")

# -------------------------merge sort - works on div & conquer

def merge_sort(arr5,arr6):
    n = m = 0
    merged = []
    while n <len(arr5) and m < len(arr6):
        if arr5[n] < arr6[m]:
            merged.append(arr5[n])
            n += 1 # but j remains same 0 ,which will be checked in next iteration
        else:
            merged.append(arr6[m])
            m += 1  # but i remains same
    while n < len(arr5):
        merged.append(arr5[n])
        n += 1
    while m < len(arr6):
        merged.append(arr6[m])
        m += 1

    return merged

ar133 = [2,4,6,12,24,28,47,51,223]
ar134 = [1,3,8,28,32,46,71]
print(merge_sort(ar133,ar134))

def rec_mergesort(arr7):
    if len(arr7) == 1:
        return arr7

    mid = len(arr7)//2

    leftarr = arr7[:mid]
    rightarr = arr7[mid:]

    leftarr = rec_mergesort(leftarr) # merge sort will work on it ,finally on both
    rightarr = rec_mergesort(rightarr)
# this wil divide the array into single unit of left and right array untill length = 1 and call merge_sort when 1
    return merge_sort(leftarr,rightarr)

ar133 = [2,4,1,6,12,8,24,11,28,47,33,51,223]
print(rec_mergesort(ar133))
# lebels of tree is logn time and merging in n so to total is nlogn
# space for array is n,recursion stack takes n space =2n - not inplace changes code,its changes is not happenning only on its own array and creating a new array on which changes happenn


def inplace_rec_mergesort(arr8,arr9,newarr):
    o = p = k= 0

    while o < len(arr8) and p < len(arr9):
        if arr8[o] < arr9[p]:
            newarr[k] = arr8[o]
            o += 1  # but j remains same 0 ,which will be checked in next iteration
        else:
            newarr[k] = arr9[p]
            p += 1  # but i remains same
        k +=1
    while o < len(arr8):
        newarr[k] = arr8[o]
        o += 1
        k+=1
    while p < len(arr9):
        newarr[k] = arr9[p]
        p += 1
        k+=1
    print(k,"k")
    return

def inplace_rec_mergesortsingle(ar7):
    if len(ar7) == 1:
        return ar7

    mid = len(ar7)//2

    leftarr1 = ar7[:mid]
    rightarr2 = ar7[mid:]

    inplace_rec_mergesortsingle(leftarr1) # merge sort will work on it ,finally on both
    inplace_rec_mergesortsingle(rightarr2)
# this wil divide the array into single unit of left and right array untill length = 1 and call merge_sort when 1
   # return inplace_rec_mergesort(leftarr1,rightarr2,ar7)
    return

ar = [2,4,1,6,12,8,24,11,28,47,33,51,223]
print(inplace_rec_mergesortsingle(ar),"inplace")






