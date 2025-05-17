
# recursion

def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    print("end") # call stack starts removing cell ofstack when call starts ending when reach  base case

show(5)
# ----------------------------
def fact(m):
    if m ==0 or m == 1:
        return  1
    else:
        #print( n * fact(n-1),end=" ")
        print(m , "*",end=" ")
        return m * fact(m-1) # until base case it calls next lower case n-1 when base case case reached it starts getting values and stack is poped

print(fact(5))

#-----------------
def cal_sum(x):
    if x == 0:
        return 0
    print(x)
    return cal_sum(x -1) + x

print(cal_sum(5))
#--------------
def print_list(list,ind):
    if ind == len(list):
        return
    print(list[ind])
    print_list(list,ind +1)

fl = [ "s","f","t","y"]
print_list(fl,0)


def print_list(list1,ind):
    if ind == len(list1):
        return 0
    print(list1[ind])
    print_list(list1,ind +1)

fl = [ "s","f","t","y"]
print_list(fl,0)














