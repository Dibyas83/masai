def exist(board, word):
    def dfs(row, col, word_index):
        if word_index == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[word_index]:
            return False

        temp = board[row][col]
        board[row][col] = '#'

        found = dfs(row + 1, col, word_index + 1) or \
                dfs(row - 1, col, word_index + 1) or \
                dfs(row, col + 1, word_index + 1) or \
                dfs(row, col - 1, word_index + 1)

        board[row][col] = temp
        return found

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(i, j, 0):
                return True
    return False

def inpt():
    t = int(input())
    for _ in range(t):
        row,col =map(int,input().split(" "))
        word =input()
        board  = [row]*[col]

        exists = exist(board,word)
        print(exists)

inpt()

"""
Grid of characters
Last Updated : 30 Sep, 2024
Given a 2D grid m*n of characters and a word, the task is to find all occurrences of the given word in the grid. A word can be matched in all 8 directions at any point. Word is said to be found in a direction if all characters match in this direction (not in zig-zag form).
The 8 directions are, Horizontally Left, Horizontally Right, Vertically Up, Vertically Down and 4 Diagonal directions.

Note: The returning list should be lexicographically smallest. If the word can be found in multiple directions starting from the same coordinates, the list should contain the coordinates only once. 

Examples: 

Input:  
grid = {{G,E,E,K,S,F,O,R,G,E,E,K,S}, {G,E,E,K,S,Q,U,I,Z,G,E,E,K}, {I,D,E,Q,A,P,R,A,C,T,I,C,E}}
word = “GEEKS”
Output: {{0,0}, {0,8}, {1,0}}


ex-3_1
Input: 
grid = {{a,b,a,b},{a,b,e,b},{e,b,e,b}}
word = “abe”
Output: 
{{0,0},{0,2},{1,0}}


2222
Try it on GfG Practice
redirect icon
Table of Content

[Naive Approach] Using Recursion – O(m*n*k) Time and O(k) Space
[Expected Approach] Using Iteration – O(m*n*k) Time and O(1) Space
[Naive Approach] Using Recursion – O(m*n*k) Time and O(k) Space
Visit each cell in the grid and check in all eight directions (up, down, left, right, and diagonals) to find the word. And for each cell, we try to move in one direction.


We keep checking, if the letter in the cell of grid matches the word as we move in the chosen direction.
If we find the whole word, we store the starting point.
We do this for every cell in the grid recursively.



# Python program to search a word in a 2D grid

# This function checks if the given
# coordinate is valid
def isValid(x, y, sizeX, sizeY):
    return 0 <= x < sizeX and 0 <= y < sizeY

def findWordInDirection(grid, n, m, word, index,
                        x, y, dirX, dirY):
    if index == len(word):
        return True

    if isValid(x, y, n, m) and word[index] == grid[x][y]:
        return findWordInDirection(grid, n, m, word, index + 1, 
                                   x + dirX, y + dirY, dirX, dirY)

    return False

def searchWord(grid, word):
    ans = []
    n = len(grid)
    m = len(grid[0])

    # Directions for 8 possible movements
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for i in range(n):
        for j in range(m):
          
            # Check if the first character matches
            if grid[i][j] == word[0]:  
                for dirX, dirY in directions:
                    if findWordInDirection(grid, n, m, word, 0, 
                                           i, j, dirX, dirY):
                        ans.append([i, j])
                        break

    return ans

def printResult(ans):
    for a in ans:
       print(f"{{{a[0]},{a[1]}}}", end=" ")
    print()

if __name__ == "__main__":
    grid = [['a', 'b', 'a', 'b'],
            ['a', 'b', 'e', 'b'],
            ['e', 'b', 'e', 'b']]
    word = "abe"

    ans = searchWord(grid, word)
    printResult(ans)

Output
{0,0} {0,2} {1,0} 
Time Complexity: O(m*n*k), where m is the number of rows, n is the number of columns and k is the length of word.
Auxiliary Space: O(k), recursion stack space.

[Expected Approach] Using Iteration – O(m*n*k) Time and O(1) Space
This is iterative approach for the above discussed recursive approach. Here, for each cell, we try to move in one direction iteratively.


We keep checking, if the letter in the cell of grid matches the word as we move in the chosen direction.
If we find the whole word, we store the starting point.
We do this for every cell in the grid.



# Python program to search word in 2D grid in 8 directions

# This function searches for the given word
# in all 8 directions from the coordinate.
def search2D(grid, row, col, word):
    m = len(grid)
    n = len(grid[0])

    # return false if the given coordinate
    # does not match with first index char.
    if grid[row][col] != word[0]:
        return False

    lenWord = len(word)

    # x and y are used to set the direction in which
    # word needs to be searched.
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]

    # This loop will search in all the 8 directions
    # one by one. It will return true if one of the
    # directions contain the word.
    for dir in range(8):

        # Initialize starting point for current direction
        currX, currY = row + x[dir], col + y[dir]
        k = 1

        while k < lenWord:

            # break if out of bounds
            if currX >= m or currX < 0 or currY >= n or currY < 0:
                break

            # break if characters dont match
            if grid[currX][currY] != word[k]:
                break

            # Moving in particular direction
            currX += x[dir]
            currY += y[dir]
            k += 1

        # If all character matched, then value of must
        # be equal to length of word
        if k == lenWord:
            return True

    # if word is not found in any direction,
    # then return false
    return False

# This function calls search2D for each coordinate


def searchWord(grid, word):
    m = len(grid)
    n = len(grid[0])

    ans = []

    for i in range(m):
        for j in range(n):

            # if the word is found from this coordinate,
                    # then append it to result.
            if search2D(grid, i, j, word):
                ans.append((i, j))

    return ans


def printResult(ans):
    for coord in ans:
        print(f"{{{coord[0]},{coord[1]}}}", end=" ")
    print()


if __name__ == "__main__":
    grid = [['a', 'b', 'a', 'b'],
            ['a', 'b', 'e', 'b'],
            ['e', 'b', 'e', 'b']]
    word = "abe"

    ans = searchWord(grid, word)

    printResult(ans)

Output
{0,0} {0,2} {1,0} 
Time complexity: O(m*n*k), where m is the number of rows, n is the number of columns and k is the length of word.
Auxiliary Space: O(1)
"""


