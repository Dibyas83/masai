def print_school():
    print(" masai")
    print("school")


print_school()
print("-----------------------------------")
def calculate(a,b,c,d,e,f,g,h):
    print((a+b+c)*(d+e+f+g+h))

calculate(2,3,4,5,6,7,8,9)

def trans_arr(arr):
    max = 0
    for i in arr:

        if i > max:
            max = i
        else:
            print(-1)
    return max


arr = [3 ,5 ,6 ,7 ,8 ,4 ,3]
h = trans_arr(arr)
print(h)

def transform_array(arr):
    n = len(arr)
    temp = arr[0]
    for i in range(1,n):
        if arr[i]>temp:
            temp=arr[i]
    for i in range(0,n):
        if arr[i]<temp:
            arr[i] = -1
    for x in arr:
        print(x,end=" ")
        print(arr)


arr = [3 ,5 ,6 ,7 ,8 ,4 ,3]
h1 = transform_array(arr)
print(h1)

def square(x):
    return x*x
print(square(2))
print(square(5))




















