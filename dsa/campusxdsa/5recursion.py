
def power(x,y):

    if x < 1:
        return 0
    elif x == 1:
        print(1)
        return 1
    else:
        prev = power(x//y,y)
        curr = prev*2
        #ct = ct + 1
        print(curr,"cur")
        #print(ct)
        return curr

x = 45
y=2
power(x,y)
"""
1=when x becomes 1
2
4
8
16
32
prev = power(45//2,2)=power(22//2,2)=power(11//2,2)=power(5//2,2)=power(2//2,2)=(x=1)
prev = 1,2,4,8,16,32
curr = 1,1*2,2*2,4*2,8*2,16*2
tc = log as it is being divided
"""

def mod(a,b):
    if b<=0:
        return  -1
    div = a//b
    return  a-div*b

def sum_digits(num):
    sum = 0
    while(num > 0):
        sum += num%10
        num /= 10

    return sum


print(123//10)
print(123/10)

# t(n) = { 3t(n-1) if n > 0 else 1}  - input is inc by 1 output multi by a factor so tc = exponential
# t(n) = { 2t(n-1) -1 if n > 0 else 1}
"""
t(n) = 3t(n-1) = 3[3t(n-2)] = 3**3[t(n-3)]....3**n[t(n-n)]
3**n[t(n-n)] = 3**n *1

t(n) = 2t(n-1) - 1 = 2[2t(n-2)-1]-1 = 2**n[t(n-n)]-2**(n-1)-2**1 -2**0
2**n[t(n-n)] -[2**n + 1] = 1  tc = constant
"""
#-------------------------powerset
"""

[1,2,3] = [] [1] [2] [1,2] [3] [1,3] [2,3] [1,2,3] output=8
[1,2] = [] [1] [2] [1,2] output = 4
[1] = [] [1] output = 2 
[0] = [] output = 0

"""

