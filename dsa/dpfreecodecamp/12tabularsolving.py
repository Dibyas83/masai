
"""
we create subproblems iteratively not recursively by building table
fib(6) = 8  array = |0|1|2|3|4|5|6| its one bigger .each subproblem corresponds to an elements of this array
its initialized with 0  => 0|0|0|0|0|0|0 then values are put in the table |0|1|1|2|3|5|8|
tc and space is n


"""
def fib(n):
    table = [0] * (n+1)
    table[0] = 1
    table[1] = 1

    for i in range(n-1):
        table[i+1] += table[i] # putting 1 or current val into next places in array
        table[i+2] += table[i]
    return table[n]
print(fib(6))

















