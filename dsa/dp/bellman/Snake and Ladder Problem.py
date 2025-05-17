

"""
Given a snake and ladder board, find the minimum number of dice throws required to reach the destination or last cell from the source or 1st cell. Basically, the player has total control over the outcome of the dice throw and wants to find out the minimum number of throws required to reach the last cell.
If the player reaches a cell which is the base of a ladder, the player has to climb up that ladder and if reaches a cell is the mouth of the snake, and has to go down to the tail of the snake without a dice throw.

Example:

Input:



snakesandladders



Output: 3
Explaination: Following are the steps:



First throw two dice to reach cell number 3 and then ladder to reach 22
Then throw 6 to reach 28.
Finally through 2 to reach 30.
There can be other solutions as well like (2, 2, 6), (2, 4, 4), (2, 3, 5).. etc.
Try it on GfG Practice
redirect icon
Snake and Ladder Problem using Breadth-First Search:
The idea is to consider the given snake and ladder board as a directed graph with a number of vertices equal to the number of cells in the board. The problem reduces to finding the shortest path in a graph. Every vertex of the graph has an edge to next six vertices if the next 6 vertices do not have a snake or ladder. If any of the next six vertices has a snake or ladder, then the edge from the current vertex goes to the top of the ladder or tail of the snake. Since all edges are of equal weight, we can efficiently find the shortest path using Breadth-First Search of the graph.



Following is the implementation of the above idea.




1
# Python3 program to find minimum number
2
# of dice throws required to reach last
3
# cell from first cell of a given
4
# snake and ladder board
5
​
6
# An entry in queue used in BFS
7
​
8
​
9
class QueueEntry(object):
10
    def __init__(self, v=0, dist=0):
11
        self.v = v
12
        self.dist = dist
13
​
14
​
15
'''This function returns minimum number of
16
dice throws required to. Reach last cell
17
from 0'th cell in a snake and ladder game.
18
move[] is an array of size N where N is
19
no. of cells on board. If there is no
20
snake or ladder from cell i, then move[i]
21
is -1. Otherwise move[i] contains cell to
22
which snake or ladder at i takes to.'''
23
​
24
​
25
def getMinDiceThrows(move, N):
26
​
27
    # The graph has N vertices. Mark all
28
    # the vertices as not visited
29
    visited = [False] * N
30
​
31
    # Create a queue for BFS
32
    queue = []
33
​
34
    # Mark the node 0 as visited and enqueue it
35
    visited[0] = True
36
​
37
    # Distance of 0't vertex is also 0
38
    # Enqueue 0'th vertex
39
    queue.append(QueueEntry(0, 0))
40
​
41
    # Do a BFS starting from vertex at index 0
42
    qe = QueueEntry()  # A queue entry (qe)
43
    while queue:
44
        qe = queue.pop(0)
45
        v = qe.v  # Vertex no. of queue entry
46
​
47
        # If front vertex is the destination
48
        # vertex, we are done
49
        if v == N - 1:
50
            break
51
​
52
        # Otherwise dequeue the front vertex
53
        # and enqueue its adjacent vertices
54
        # (or cell numbers reachable through
55
        # a dice throw)
56
        j = v + 1
57
        while j <= v + 6 and j < N:
58
​
59
            # If this cell is already visited,
60
            # then ignore
61
            if visited[j] is False:
62
​
63
                # Otherwise calculate its
64
                # distance and mark it
65
                # as visited
66
                a = QueueEntry()
67
                a.dist = qe.dist + 1
68
                visited[j] = True
69
​
70
                # Check if there a snake or ladder
71
                # at 'j' then tail of snake or top
72
                # of ladder become the adjacent of 'i'
73
                a.v = move[j] if move[j] != -1 else j
74
​
75
                queue.append(a)
76
​
77
            j += 1
78
​
79
    # We reach here when 'qe' has last vertex
80
    # return the distance of vertex in 'qe
81
    return qe.dist
82
​
83
​
84
# driver code
85
N = 30
86
moves = [-1] * N
87
​
88
# Ladders
89
moves[2] = 21
90
moves[4] = 7
91
moves[10] = 25
92
moves[19] = 28
93
​
94
# Snakes
95
moves[26] = 0
96
moves[20] = 8
97
moves[16] = 3
98
moves[18] = 6
99
​
100
print("Min Dice throws required is {0}".
101
      format(getMinDiceThrows(moves, N)))
102
​
103
# This code is contributed by Ajitesh Pathak

Output
Min Dice throws required is 3
Time complexity: O(N) as every cell is added and removed only once from the queue. And a typical enqueue or dequeue operation takes O(1) time.
Auxiliary Space : O(N)

Snake and Ladder Problem using Recursion:
We can think of is recursion in which we will be going to each block, in this case, which is from 1 to 30, and keeping a count of a minimum number of throws of dice at block i and storing it in an array t.



So, basically, we will:



Create an array, let’s say ‘t’, and initialize it with -1.
Now we will call a recursive function from block 1, with variable let’s say ‘i’, and we will be incrementing this.
In this we will define the base condition as whenever block number reaches 30 or beyond we will return 0 and we will also check if this block has been visited before, this we will do by checking the value of t[i], if this is -1 then it means its not visited and we move forward with the function else its visited and we will return value of t[i].
 After checking base cases we will initialize a variable ‘min’ with a max integer value.
Now we will initiate a loop from 1 to 6, i.e the values of a dice, now for each iteration we will increase the value of i by the value of dice(eg: i+1,i+2….i+6) and we will check if any increased value has a ladder on it if there is then we will update the value of i to the end of the ladder and then pass the value to the recursive function, if there is no ladder then also we will pass the incremented value of i based on dice value to a recursive function, but if there is a snake then we won’t pass this value to recursive function as we want to reach the end as soon as possible, and the best of doing this would be not to be bitten by a snake. And we would be keep on updating the minimum value for variable ‘min’.
Finally we will update t[i] with min and return t[i].
Below is the implementation of the above approach:




1
from typing import List, Dict
2
​
3
​
4
def min_throw(n: int, arr: List[int]) -> int:
5
    # Initialise an array t of length 31, we will use from
6
    # index to 1 to 30
7
    t = [-1] * 31
8
​
9
    # create a dictionary to store snakes and ladders start
10
    # and end for better efficiency
11
    h = {}
12
    for i in range(0, 2 * n, 2):
13
        # store start as key and end as value
14
        h[arr[i]] = arr[i + 1]
15
​
16
    # final ans
17
    return sol(1, h, t)
18
​
19
# recursive function
20
​
21
​
22
def sol(i: int, h: Dict[int, int], t: List[int]) -> int:
23
    # base condition
24
    if i >= 30:
25
        return 0
26
​
27
    # checking if block is already visited or
28
    # not(memoization).
29
    elif t[i] != -1:
30
        return t[i]
31
​
32
    # initialising min as max int value
33
    min_value = float("inf")
34
​
35
    # for loop for every dice value from 1 to 6
36
    for j in range(1, 7):
37
        # incrementing value of i with dice value i.e j
38
        # taking new variable k
39
        # ->taking new variable so that we dont change i
40
        # as we will need it again in another iteration
41
        k = i + j
42
        if k in h:
43
            # checking if this is a snake or ladder
44
            # if a snake then we continue as we dont
45
            # need a snake
46
            if h[k] < k:
47
                continue
48
            # updating if it's a ladder to ladder end value
49
            k = h[k]
50
        # updating min in every iteration for getting
51
        # minimum throws from this particular block
52
        min_value = min(min_value, sol(k, h, t) + 1)
53
​
54
    # updating value of t[i] to min
55
    # memoization
56
    t[i] = min_value
57
    return t[i]
58
​
59
​
60
# Given a 5x6 snakes and ladders board
61
# You are given an integer N denoting the total
62
# number of snakes and ladders and a list arr[]
63
# of 2*N size where 2*i and (2*i + 1)th values
64
# denote the starting and ending point respectively
65
# of ith snake or ladder
66
N = 8
67
arr = [3, 22, 5, 8, 11, 26, 20, 29, 17, 4, 19, 7, 27, 1, 29, 9]
68
​
69
print("Min Dice throws required is", min_throw(N, arr))
70
# This code is contributed by sanjanasikarwar24

Output
Min Dice throws required is 3
Time complexity: O(N).
Auxiliary Space O(N)


"""









