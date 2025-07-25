
def multiply(a,b):
    res = 0
    for i in range(b):
        res+=a
    print(res)

multiply(5,6)

# in recursive -1 find base case 2- differentiate breakdown it to base case
# 4,4(a,b) = 4 + 3*4 =4+4+2*4=4+4+4 + 1*4  = when b =1 ans is a
def mul(a,b):
    if b==1:
        return a
    else:
        return a + mul(a,b-1)# breakdown to base case  and keep checking if b=1 ,when b =1 it gets ans a ,which was called by return a+a+....mul(a,2-1) .so the value goes to prev call
print(mul(7,8))
# this is like stack the func that formed first was solved last , the last func was solved first which becomes the value for prev func

def fact(aa):
    if aa==1:
        return 1
    else:
        return aa * fact(aa-1) # gives aa+ ((aa-1) + fact(aa-1-1))


def palindrome(madam):
    mid = len(madam) // 2
    if len(madam)%2 == 0:
        mid = mid-1
        if madam[mid] == madam[mid + 1]:
            return True
        elif madam[mid] != madam[mid + 1]:
            return False
    if madam[mid-1] == madam[mid+1]:
        return True
    elif madam[mid-1] != madam[mid+1]:
        return False
    else:
        for i in range(len(madam)):
            return palindrome(madam[i:-(i+1)])
    if False in palindrome(madam):
        return False
    else:
        return True

print(palindrome("abcjicba"))

def pal(stri):
    if len(stri) <= 1: # for 0 and 1
        print("palind")
    else:# if length is not 1 match first and last if same reduce string size
        if stri[0] == stri[-1]:
            pal(stri[1:-1]) # it makes it iterative as next stri in pal will come reduced
        else:
            print("not pal")

pal("abba")
pal("abcba")

# rabbit problem -a pair rabit by 2nd month will start produce anather pair  every month
"""
there was one pair
month0- 1pair
month1 - 1 pair a
month2 - 2 pair a,b   - starts inc only after 2 month so takes two fib
month3 -3 pair a+1,b
month4 - 5 pair a+1+c,b+1
--------------------------------
taking 3 mnt to produce
month0 - 1a
month1 - 1a=1+0
month2 - 1a=1+0
month3 - 2a+b=1+1
month4 - 3a+c+b=2+1
month5 - 4a+c+d+b=3+1
month6 - 6(a+c+d+e) +(b+f)=4+2
month7 - 9(a+(c+g)+d+e+x) +(b+f+h)=6+3
month8 - 13(a+i+(c+g+j)+(d+k)+e+x) +(b+f+h+l)=9+4
month9 - 19(a+i+m+(b+(f+q)+h+l+r)+(c+g+j+n)+(d+k+o)+(e+p)+x ) -> a6 + b4 +c3 +d2 +e1 = 13 +6=9+6+4
fib(m-2) + fib(m-3) +fib(m-4)
"""
def fib(m): # m= month
    if m == 0 or m==1:
        return 1
    else:
        return fib(m-1) + fib(m-2)  #like summation find the base case then sum.it will solve for a,then a's child b,then for a's child c and b's child d ......
print(fib(11))

# tc is 2**n exponential.it needs value of two other,these two will take 2 each.so the first needs 4 input or more according to the no levels each twice the size below it.
#fib8-fib7+fib6
# to reduce the time taken we use dynamic programming or memoization,but little more space required



















