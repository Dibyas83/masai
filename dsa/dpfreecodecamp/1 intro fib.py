
"""
dp
1 memoization
2 tabulation

"""
# getting nth fib no
def fib(n):
    if n <=2:
        return 1
    else:
        return fib(n-1) + fib(n-2)# like produce after 2 month and produce after 1 month

print(fib(5))

def foo(n1):
    if n1 <= 1:
        return 1
    else:
        return n1 + foo(n1 - 1)

print(foo(5))
# tc n**n ,space complxity = n  no of levels = n/2=n

def fibmemo(n,dict):

    if n in dict:
        return dict[n]
    if n <=2: # at very end n will become 2 then 1,till then all func n-1,n-2,n-3 .....2,1 will be
        # stored in dict they then 2 and 1 will return 1 each,when it reaches 2 it returns 1 and poped
        # then it reaches 1 it returns 1 and pops then dict[3] stores 2 and func3 pops from stack .it
        # reaches n and ans returned
        return 1
    else:
        dict[n] = fibmemo(n-1,dict) + fibmemo(n-2,dict)
        return dict[n] # like produce after 2 month and produce after 1 month
d= {}
print(fibmemo(10,d),"m")











