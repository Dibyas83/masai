

"""
Maximum number of customers that can be satisfied with given quantity
Last Updated : 28 Nov, 2022
A new variety of rice has been brought in supermarket and being available for the first time, the quantity of this rice is limited. Each customer demands the rice in two different packaging of size a and size b. The sizes a and b are decided by staff as per the demand. Given the size of the packets a and b, the total quantity of rice available d and the number of customers n, find out maximum number of customers that can be satisfied with the given quantity of rice. Display the total number of customers that can be satisfied and the index of customers that can be satisfied.

Note: If a customer orders 2 3, he requires 2 packets of size a and 3 packets of size b. Assume indexing of customers starts from 1.

Input: The first line of input contains two integers n and d; next line contains two integers a and b. Next n lines contain two integers for each customer denoting total number of bags of size a and size b that customer requires.
Output: Print the maximum number of customers that can be satisfied and in the next line print the space-separated indexes of satisfied customers.

Examples:

Input : n = 5, d = 5
        a = 1, b = 1
        2 0
        3 2
        4 4
        10 0
        0 1
Output : 2
         5 1

Input : n = 6, d = 1000000000
       a = 9999, b = 10000
       10000 9998
       10000 10000
       10000 10000
       70000 70000
       10000 10000
       10000 10000
Output : 5
         1 2 3 5 6
Explanation: In first example, the order of customers according to their demand is:

Customer ID   Demand
   5            1
   1            2
   2            5
   3            8
   4            10
From this, it can easily be concluded that only customer 5 and customer 1 can be satisfied for total demand of 1 + 2 = 3. Rest of the customer cannot purchase the remaining rice, as their demand is greater than available amount.

Approach: In order to meet the demand of maximum number of customers we must start with the customer with minimum demand so that we have maximum amount of rice left to satisfy remaining customers. Therefore, sort the customers according to the increasing order of demand so that maximum number of customers can be satisfied. Below is the implementation of above approach:

Implementation:




# Python3 program to find maximum number
# of customers that can be satisfied
v = []

# print maximum number of satisfied
# customers and their indexes
def solve(n, d, a, b, arr):
    first, second = 0, 1

    # Creating an vector of pair of
    # total demand and customer number
    for i in range(n):
        m = arr[i][0]
        t = arr[i][1]
        v.append([a * m + b * t, i + 1])

    # Sorting the customers according
    # to their total demand
    v.sort()

    ans = []

    # Taking the first k customers that
    # can be satisfied by total amount d
    for i in range(n):
        if v[i][first] <= d:
            ans.append(v[i][second])
            d -= v[i][first]

    print(len(ans))
    for i in range(len(ans)):
        print(ans[i], end = " ")

# Driver Code
if __name__ == '__main__':

    # Initializing variables
    n = 5
    d = 5
    a = 1
    b = 1
    arr = [[2, 0], [3, 2],
           [4, 4], [10, 0],
           [0, 1]]

    solve(n, d, a, b, arr)

# This code is contributed by PranchalK
Output
2
5 1
Time Complexity: O(n*log(n))
Auxiliary Space: O(n)



"""









