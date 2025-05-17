
"""

There is a stack of water glasses in the form of a Pascal triangle and a person wants to pour the water at the topmost glass, but the capacity of each glass is 1 unit. Overflow occurs in such a way that after 1 unit, 1/2 of the remaining unit gets into the bottom left glass and the other half in the bottom right glass. We pour k units of water into the topmost glass. The task is to find how much water is there in the c’th glass of the r’th row.

Note: Assume that there are enough glasses in the triangle till no glass overflows.

Example:

Input: k = 3, r = 2, c = 1
Output: 1.000000
Explanation: After the first glass, 2 units of water will remain and they will spread equally on the two glasses on the second row. Therefore, the glass on the 2nd row and 1st column will have 1 unit of water.


water-overflow-1



Input: k = 2, r = 2, c = 2
Output: 0.5
Explanation: After the first glass, 1 units of water will remain and they will spread equally on the two glasses on the second row. Therefore, the glass on the 2nd row and 2nd column will have half unit of water.


water-overflow-2
Try it on GfG Practice
redirect icon
Table of Content

Using Dynamic Programming – O(r^2) time and O(r^2) Space
Using Queue – O(r^2) Time and O(r) Space
Using Dynamic Programming – O(r^2) time and O(r^2) Space
 The approach to solving the water overflow problem involves simulating water distribution through a grid-based representation of a Pascal triangle  of glasses. The process starts by pouring a given amount of water into the top glass. Then, for each glass, the algorithm checks if the water exceeds the glass’s capacity of 1 unit. If overflow occurs, the excess water is evenly distributed to the two glasses directly below. Each glass is capped at a maximum of 1 unit. This process is repeated iteratively until the target row is reached. The final result is the amount of water in the specified glass, ensuring no glass exceeds its maximum capacity.





1
# Python program to find amount
2
# of water in a given glass Using Dynamic Programming
3
​
4
def waterOverflow(k, r, c):
5

6
    # DP matrix to simulate water flow in glasses
7
    memo = [[0.0 for _ in range(r)] for _ in range(r)]
8

9
    # Initial water in top glass
10
    memo[0][0] = k
11

12
    # Simulate water flow through triangle
13
    for row in range(r - 1):
14
        for col in range(row + 1):
15

16
            # Calculate water overflow
17
            excess = max(0.0, memo[row][col] - 1.0)
18

19
            # Distribute excess water
20
            if excess > 0:
21

22
                # Cap current glass
23
                memo[row][col] = 1.0
24

25
                # Flow to bottom glasses
26
                memo[row + 1][col] += excess / 2.0
27
                memo[row + 1][col + 1] += excess / 2.0
28

29
    # Return water in target glass
30
    return min(1.0, memo[r - 1][c - 1])
31
​
32
​
33
if __name__ == "__main__":
34
    k = 3
35
    r = 2
36
    c = 1
37

38
    waterAmount = waterOverflow(k, r, c)
39
    print(waterAmount)

Output
1
Using Queue – O(r^2) Time and O(r) Space
The approach simulates the water overflow process using a queue to track water distribution through a Pascal triangle of glasses. The algorithm processes glasses row by row, managing overflow by distributing excess water equally to the glasses below. It ensures that no glass exceeds its 1-unit capacity, using the queue to efficiently handle water amounts and overflow at each step. The water in each glass is updated progressively, and the target glass’s water amount is returned once the process reaches the specified row and column.





1
# Python program to find amount
2
# of water in a given glass using queue
3
from collections import deque
4
​
5
def waterOverflow(k, r, c):
6

7
    # Adjust row and column to 0-based indexing
8
    r -= 1
9
    c -= 1
10
​
11
    # Initialize queue with total water units
12
    q = deque([1.0 * k])
13
​
14
    # Variable to track overflow from previous glasses
15
    prev = 0
16
​
17
    # Simulate water flow row by row
18
    for i in range(r + 1):
19

20
        # Process current row's glasses
21
        size = len(q)
22
        for j in range(size):
23

24
            # Get current glass water amount
25
            curr = q.popleft()
26
​
27
            # Check if target glass is reached
28
            if i == r and j == c:
29
                return min(curr, 1.0)
30
​
31
            # Reduce water in current glass
32
            curr -= 1
33
​
34
            # Calculate and distribute overflow
35
            val = max(curr / 2.0, 0.0) + prev
36
            q.append(val)
37
​
38
            # Track overflow for next iteration
39
            prev = max(0.0, curr / 2.0)
40
​
41
        # Add previous row's overflow to next row
42
        q.append(prev)
43
        prev = 0
44
​
45
    return 0
46
​
47
if __name__ == "__main__":
48
    k = 3
49
    r = 2
50
    c = 1
51
    print(waterOverflow(k, r, c))

Output
1
"""





