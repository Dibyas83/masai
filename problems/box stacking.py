# Python program to implement
# box stacking problem

# function to find the maximum height
# with box i as base.
def maxHeightRecur(i, boxes):
    ans = boxes[i][2]

    # Check all the next boxes
    for j in range(i + 1, len(boxes)):

        # If size of box j is less than
        # size of box i.
        if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
            ans = max(ans, boxes[i][2] + maxHeightRecur(j, boxes))

    return ans


def maxHeight(height, width, length):
    n = len(height)

    # Create a 2d array to store all
    # orientations of boxes in (l, b, h)
    # manner.
    boxes = []
    for i in range(n):
        a, b, c = height[i], width[i], length[i]

        boxes.append([a, b, c])
        boxes.append([a, c, b])
        boxes.append([b, a, c])
        boxes.append([b, c, a])
        boxes.append([c, a, b])
        boxes.append([c, b, a])

    # Sort the boxes in descending
    # order of length and width.
    boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)

    ans = 0

    # Check for all boxes starting as base.
    for i in range(len(boxes)):
        ans = max(ans, maxHeightRecur(i, boxes))

    return ans


if __name__ == "__main__":
    height = [4, 1, 4, 10]
    width = [6, 2, 5, 12]
    length = [7, 3, 6, 32]

    print(maxHeight(height, width, length))
"""
Box Stacking Problem
Last Updated : 02 Dec, 2024
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





# Python program to implement
# box stacking problem

# function to find the maximum height
# with box i as base.
def maxHeightRecur(i, boxes):
    ans = boxes[i][2]

    # Check all the next boxes 
    for j in range(i + 1, len(boxes)):

        # If size of box j is less than
        # size of box i.
        if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
            ans = max(ans, boxes[i][2] + maxHeightRecur(j, boxes))

    return ans

def maxHeight(height, width, length):
    n = len(height)

    # Create a 2d array to store all 
    # orientations of boxes in (l, b, h)
    # manner.
    boxes = []
    for i in range(n):
        a, b, c = height[i], width[i], length[i]
        
        boxes.append([a, b, c])
        boxes.append([a, c, b])
        boxes.append([b, a, c])
        boxes.append([b, c, a])
        boxes.append([c, a, b])
        boxes.append([c, b, a])

    # Sort the boxes in descending 
    # order of length and width.
    boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)

    ans = 0

    # Check for all boxes starting as base.
    for i in range(len(boxes)):
        ans = max(ans, maxHeightRecur(i, boxes))

    return ans

if __name__ == "__main__":
    height = [4, 1, 4, 10]
    width = [6, 2, 5, 12]
    length = [7, 3, 6, 32]

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



# Python program to implement
# box stacking problem

def maxHeightRecur(i, boxes, memo):
  
    # If value is memoized
    if memo[i] != -1:
        return memo[i]
    
    ans = boxes[i][2]
    
    # Check all the next boxes 
    for j in range(i + 1, len(boxes)):
        
        # If size of box j is less than
        # size of box i.
        if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
            ans = max(ans, boxes[i][2] + maxHeightRecur(j, boxes, memo))
    
    memo[i] = ans
    return ans

def maxHeight(height, width, length):
    n = len(height)
    
    # Create a 2d array to store all 
    # orientations of boxes in (l, b, h)
    # manner.
    boxes = []
    for i in range(n):
        a, b, c = height[i], width[i], length[i]
        
        boxes.append([a, b, c])
        boxes.append([a, c, b])
        boxes.append([b, a, c])
        boxes.append([b, c, a])
        boxes.append([c, a, b])
        boxes.append([c, b, a])
    
    # Sort the boxes in descending 
    # order of length and width.
    boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    memo = [-1] * len(boxes)
    
    ans = 0
    
    # Check for all boxes starting as base.
    for i in range(len(boxes)):
        ans = max(ans, maxHeightRecur(i, boxes, memo))
    
    return ans

if __name__ == "__main__":
    height = [4, 1, 4, 10]
    width = [6, 2, 5, 12]
    length = [7, 3, 6, 32]
    
    print(maxHeight(height, width, length))

Output
60
Using Bottom-Up DP (Tabulation) – O(n^2) Time and O(n) Space 
 The idea is to fill the DP table from bottom to up. The table is filled in an iterative manner from i = n-1 to i = 0. For each box i, The dynamic programming relation is as follows: 


set dp[i] = height[i]
For j > i and base of j is smaller than base of i, set dp[i] = max(dp[i], height[i] + dp[j]).



# Python program to implement
# box stacking problem

def maxHeight(height, width, length):
    n = len(height)
    
    # Create a 2d array to store all 
    # orientations of boxes in (l, b, h)
    # manner.
    boxes = []
    for i in range(n):
        a, b, c = height[i], width[i], length[i]
        
        boxes.append([a, b, c])
        boxes.append([a, c, b])
        boxes.append([b, a, c])
        boxes.append([b, c, a])
        boxes.append([c, a, b])
        boxes.append([c, b, a])
    
    # Sort the boxes in descending 
    # order of length and width.
    boxes.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    dp = [0] * len(boxes)
    
    ans = 0
    
    # Check for all boxes starting as base.
    for i in range(len(boxes) - 1, -1, -1):
        dp[i] = boxes[i][2]
        
        for j in range(i + 1, len(boxes)):
            if boxes[i][0] > boxes[j][0] and boxes[i][1] > boxes[j][1]:
                dp[i] = max(dp[i], boxes[i][2] + dp[j])
        
        ans = max(ans, dp[i])
    
    return ans

if __name__ == "__main__":
    height = [4, 1, 4, 10]
    width = [6, 2, 5, 12]
    length = [7, 3, 6, 32]
    
    print(maxHeight(height, width, length))

Output
60

"""