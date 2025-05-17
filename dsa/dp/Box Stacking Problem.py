

"""
Given three arrays height[], width[], and length[] of size n, where height[i], width[i], and length[i] represent the dimensions of a box. The task is to create a stack of boxes that is as tall as possible, but we can only stack a box on top of another box if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box.

Note:

We can rotate a box so that any side functions as its base.
It is also allowable to use multiple instances of the same type of box.
The base of the lower box should be strictly larger than that of the new box we’re going to place. This is in terms of both length and width, not just in terms of area. So, two boxes with the same base cannot be placed one over the other.
Example:

Input: height[] = [4, 1, 4, 10], width[] = [6, 2, 5, 12], length[] = [7, 3, 6, 32]
Output: 60
Explanation: One way of placing the boxes is as follows in the bottom to top manner: (Denoting the boxes in (l, w, h) manner)
(12, 32, 10) (10, 12, 32) (6, 7, 4)
(5, 6, 4) (4, 5, 6) (2, 3, 1) (1, 2, 3)
Hence, the total height of this stack is 10 + 32 + 4 + 4 + 6 + 1 + 3 = 60.
No other combination of boxes produces a height greater than this.


Input: height[] = [1, 4, 3], width[] = [2, 5, 4], length[] = [3, 6, 1]
Output: 15
Explanation: One way of placing the boxes is as follows in the bottom to top manner: (Denoting the boxes in (l, w, h) manner)
(5, 6, 4) (4, 5, 6) (3, 4, 1), (2, 3, 1)
(1, 2, 3).
Hence, the total height of this stack is 4 + 6 + 1 + 1 + 3 = 15
No other combination of boxes produces a height greater than this.


Try it on GfG Practice
redirect icon
Main Idea
The Box Stacking problem is a variation of LIS problem. The main idea is to maximize the height of the stack by considering all possible orientations of the boxes and find the optimal stacking order. For each box, we generate all six possible rotations by treating each dimension as the height once, and the remaining two dimensions as the base dimensions (width and depth). By doing this, we account for all possible orientations and allow multiple instances of the same box type in different orientations.

We then sort these box rotations by their length and breath in descending order, ensuring that smaller boxes are only placed on larger ones. We compute the maximum stack height for each box as the base by iterating through all prior boxes and checking if they can be stacked. This approach ensures that we evaluate all valid stacking combinations efficiently and find the maximum height achievable.

Table of Content

Using Recursion – O(n^n) Time and O(n) Space
Using Top-Down DP (Memoization) – O(n^2) Time and O(n) Space
Using Bottom-Up DP (Tabulation) – O(n^2) Time and O(n) Space
Using Recursion – O(n^n) Time and O(n) Space
The idea is to recursively compute the maximum stack height starting from each box in all its possible orientations.


For a given box i with a particular orientation, the recursive relation is based on two conditions:


We check if the current box i can be placed on top of any previously considered box j, meaning the base of box i must be strictly smaller than the base of box j.
We compute the maximum stack height by choosing the best possible prior box to place under box i.
The recurrence relation can be written as:


maxHeight[i] = max⁡(height[i] + maxHeight[j] for all boxes j where base of box i > base of box j)
Here, maxHeight[i] represents the maximum height of the stack starting with box i in its current orientation. The recurrence works by checking all possible box placements and taking the maximum value among them, ensuring that the box stack grows in height as much as possible.


The base case is that a box by itself contributes a stack height of height[i], i.e., maxHeight[i] = height[i], when no boxes can be placed under it.





1
# Python program to implement
2
# box stacking problem
3
​
4
# function to find the maximum height
5
# with box i as base.
6
def maxHeightRecur(i, boxes):
7
    ans = boxes[i][2]
8
​
9
    # Check all the next boxes
10
    for j in range(i + 1, len(boxes)):
11
​
12
        # If size of box j is less than
13
        # size of box i.
14
        if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
15
            ans = max(ans, boxes[i][2] + maxHeightRecur(j, boxes))
16
​
17
    return ans
18
​
19
def maxHeight(height, width, length):
20
    n = len(height)
21
​
22
    # Create a 2d array to store all
23
    # orientations of boxes in (l, b, h)
24
    # manner.
25
    boxes = []
26
    for i in range(n):
27
        a, b, c = height[i], width[i], length[i]
28

29
        boxes.append([a, b, c])
30
        boxes.append([a, c, b])
31
        boxes.append([b, a, c])
32
        boxes.append([b, c, a])
33
        boxes.append([c, a, b])
34
        boxes.append([c, b, a])
35
​
36
    # Sort the boxes in descending
37
    # order of length and width.
38
    boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)
39
​
40
    ans = 0
41
​
42
    # Check for all boxes starting as base.
43
    for i in range(len(boxes)):
44
        ans = max(ans, maxHeightRecur(i, boxes))
45
​
46
    return ans
47
​
48
if __name__ == "__main__":
49
    height = [4, 1, 4, 10]
50
    width = [6, 2, 5, 12]
51
    length = [7, 3, 6, 32]
52
​
53
    print(maxHeight(height, width, length))

Output
60
Using Top-Down DP (Memoization) – O(n^2) Time and O(n) Space
If we notice carefully, we can observe that the above recursive solution holds the following two properties of Dynamic Programming:

1. Optimal Substructure: Maximum height of box stack at index i, i.e., maxHeight(i), depends on the optimal solutions of the subproblems maxHeight(j) for all j > i and base of j is smaller than i. By comparing these optimal substructures, we can efficiently calculate the maximum height of box stack at index i.


2. Overlapping Subproblems: While applying a recursive approach in this problem, we notice that certain subproblems are computed multiple times.


There is only one parameter: i that changes in the recursive solution. So we create a 1D array of size 6*n for memorization (since there are 6 possible orientations for each box). Therefore, memo[i] stores the result for the i-th box in the sorted list of orientations.
We initialize this array as -1 to indicate nothing is computed initially.
Now we modify our recursive solution to first check if the value is -1, then only make recursive calls. This way, we avoid re-computations of the same subproblems.



1
# Python program to implement
2
# box stacking problem
3
​
4
def maxHeightRecur(i, boxes, memo):
5

6
    # If value is memoized
7
    if memo[i] != -1:
8
        return memo[i]
9

10
    ans = boxes[i][2]
11

12
    # Check all the next boxes
13
    for j in range(i + 1, len(boxes)):
14

15
        # If size of box j is less than
16
        # size of box i.
17
        if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
18
            ans = max(ans, boxes[i][2] + maxHeightRecur(j, boxes, memo))
19

20
    memo[i] = ans
21
    return ans
22
​
23
def maxHeight(height, width, length):
24
    n = len(height)
25

26
    # Create a 2d array to store all
27
    # orientations of boxes in (l, b, h)
28
    # manner.
29
    boxes = []
30
    for i in range(n):
31
        a, b, c = height[i], width[i], length[i]
32

33
        boxes.append([a, b, c])
34
        boxes.append([a, c, b])
35
        boxes.append([b, a, c])
36
        boxes.append([b, c, a])
37
        boxes.append([c, a, b])
38
        boxes.append([c, b, a])
39

40
    # Sort the boxes in descending
41
    # order of length and width.
42
    boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)
43

44
    memo = [-1] * len(boxes)
45

46
    ans = 0
47

48
    # Check for all boxes starting as base.
49
    for i in range(len(boxes)):
50
        ans = max(ans, maxHeightRecur(i, boxes, memo))
51

52
    return ans
53
​
54
if __name__ == "__main__":
55
    height = [4, 1, 4, 10]
56
    width = [6, 2, 5, 12]
57
    length = [7, 3, 6, 32]
58

59
    print(maxHeight(height, width, length))

Output
60
Using Bottom-Up DP (Tabulation) – O(n^2) Time and O(n) Space
 The idea is to fill the DP table from bottom to up. The table is filled in an iterative manner from i = n-1 to i = 0. For each box i, The dynamic programming relation is as follows:


set dp[i] = height[i]
For j > i and base of j is smaller than base of i, set dp[i] = max(dp[i], height[i] + dp[j]).



1
# Python program to implement
2
# box stacking problem
3
​
4
def maxHeight(height, width, length):
5
    n = len(height)
6

7
    # Create a 2d array to store all
8
    # orientations of boxes in (l, b, h)
9
    # manner.
10
    boxes = []
11
    for i in range(n):
12
        a, b, c = height[i], width[i], length[i]
13

14
        boxes.append([a, b, c])
15
        boxes.append([a, c, b])
16
        boxes.append([b, a, c])
17
        boxes.append([b, c, a])
18
        boxes.append([c, a, b])
19
        boxes.append([c, b, a])
20

21
    # Sort the boxes in descending
22
    # order of length and width.
23
    boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)
24

25
    dp = [0] * len(boxes)
26

27
    ans = 0
28

29
    # Check for all boxes starting as base.
30
    for i in range(len(boxes) - 1, -1, -1):
31
        dp[i] = boxes[i][2]
32

33
        for j in range(i + 1, len(boxes)):
34
            if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
35
                dp[i] = max(dp[i], boxes[i][2] + dp[j])
36

37
        ans = max(ans, dp[i])
38

39
    return ans
40
​
41
if __name__ == "__main__":
42
    height = [4, 1, 4, 10]
43
    width = [6, 2, 5, 12]
44
    length = [7, 3, 6, 32]
45

46
    print(maxHeight(height, width, length))

Output
60



"""










