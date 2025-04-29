

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
def inpt():
    t = int(input())
    for _ in range(t):
        row, col = map(int, input().split(" "))
        grid = []
        for i in range(row):  # A for loop for row entries
            a = []
            for j in range(col):  # A for loop for column entries
                a.append(input())
            grid.append(a)
        word = input()

        ans = search2D(grid, row, col, word)
        print(ans)
inpt()




