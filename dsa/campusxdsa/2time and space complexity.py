
def facto(n):
    ans = 1        #  1
    while n>1:      #  n
        ans *= n    #
        n -= 1      #
    return ans
n=5
print(facto(n))

#   n**2(for loop)  +  2n(calculations inside loop)  +  2(outside loop operations or constants)

#quadratic relationship- input 3,4times inc time inc by 9,16times
"""
1    -constant  ex by x[index]  dict - ist mem addres + 4bytes *index no - no dependent on input
n   - linear  ex linear search in array of size n ,needs n comparison
n**2    -quadratic  ex using nested loop in sorting algorithms as bubble
logn  < n - logarthmic  ex timetaken dec as  input inc - as in binary search. inp 10  100  1000,time 1 2 3
n     < nlogn     -nlogn   ex merge sort,quick sort
n**20(polynomial) < 3**n -exponen   exp is opposite of logn- inp 1 2 3 4 time 1 10 100 1000

inp         10      100     1000
O(1)        1       1       1
O(logn)     1       2       3
O(n)        10      100     1000
O(nlogn)    10      200     3000
O(n**n)     100     10000   1000000
O(2**n)     1024    1267506002277979979  143972747236978469321786492736492786349726349296327639279236722

"""

l =[1,2,3,4,5]
for i in l:
    for j in l:
        print('({},{})'.format(i,j))

