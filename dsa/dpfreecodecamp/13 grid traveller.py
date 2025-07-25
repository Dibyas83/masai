
"""
in a 0/0 grid theres 0 way to move
if any dimensioms contain 0 ,means  it is empty

add value of your cur pos to the next position you can move  ie is down and right
grid(3,3)   ->    0|0|0|0   initialized with 0
                  0|1|0|0   1 at 1,1  the starting point ,from 1 it will contribute 1 to right and down.at end it will get 6
                  0|0|0|0
                  0|0|0|0
grid(1,1) returns 1 way
grid(0,0) returns 0 way

 time mn and space mn

def grtrav2(m, n):
    table = [[''] * (n + 1) for _ in range(m + 1)]  # multiple arrays appended

    table[0][0] = 'x'
    print(table)


print(grtrav2(3, 2))


def grtrav3(m, n):
    table = [[None] * (n + 1) for _ in range(m + 1)]

    table[0][0] = 'x'
    print(table)


print(grtrav3(3, 2))
"""

"""
def grtrav(m, n):
    table = [[None for _ in range(n + 1)] for _ in range(m + 1)]

    table[0][0] = 'x'
    print(table)

print(grtrav(3, 2))
"""
def grtrav(m, n):
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            current = table[i][j]
            if j + 1 <= n: # doesnot goes outside
                table[i][j + 1] += current  # adding to right , j is col
            if i + 1 <= m:
                table[i + 1][j] += current  # adding to down

    return table[m][n]

print(grtrav(1, 1))
print(grtrav(2, 3))
print(grtrav(3, 2))
print(grtrav(3, 3))
print(grtrav(18, 18))

"""
1 -visualize the problem as a table
2 - size the table based on the inputs
3 - initialize the table with default values
4 - seed the trivial answer(like 1) into the table
5 - iterate through the table
6 -fill further positions based on the current position
"""







