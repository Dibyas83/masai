
#Question 1




def fun1(x, y) :

    if (x == 0) :
        return y
    else :
        return fun1(x - 1, x + y)  # 5+2->4+5+2->3+4+5+2->2+3+4+5+2->1+2+3+4+5+2

x,y = map(int,input().split(" "))
print(fun1(x,y))

"""

Answer: The function fun1() calculates and returns ((1 + 2 … + x-1 + x) +y), which is x(x + 1) / 2 + y.For
example,
if x is 5 and y is 2, then fun should return 15 + 2 = 17.

Question
2
"""

# Minimum index finder
def minIndex(arr, s, e):
    sml = sys.maxsize
    mindex = 0

    for i in range(s, e):
        if (sml > arr[i]):
            sml = arr[i]
            mindex = i

    return mindex


def fun2(arr, start_index, end_index):
    if (start_index >= end_index):
        return

    # minIndex() returns index of minimum value in
    # array arr[start_index...end_index]
    min_index = minIndex(arr, start_index, end_index)
    arr[start_index], arr[min_index] = arr[min_index], arr[start_index]
    fun2(arr, start_index + 1, end_index)


"""

Answer: The function fun2() is a recursive implementation of SelectionSort.

Time
complexity: O(N2)
Auxiliary
Space: O(1)

"""







