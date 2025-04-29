import numpy as np

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # Depth-first search function to search the word in the board
        def search_word(x: int, y: int, index: int) -> bool:
            # Check if the last character matches
            if index == len(word) - 1:
                return board[x][y] == word[index]
            # If current character does not match the word character at index, return False
            if board[x][y] != word[index]:
                return False
            # Store the current character and mark the cell as visited with "0"
            temp = board[x][y]
            board[x][y] = "0"
            # Define directions for exploration: up, right, down, left
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            # Loop through all possible directions
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                # Check boundaries and if the next cell is not visited
                if 0 <= new_x < rows and 0 <= new_y < cols and board[new_x][new_y] != "0":
                    # Recur with the new position and the next character index
                    if search_word(new_x, new_y, index + 1):
                        return True
            # Restore the current cell's value after exploring all directions
            board[x][y] = temp
            return False

        # Retrieve the dimensions of the board
        rows, cols = len(board), len(board[0])
        # Iterate through each cell in the board, trying to match the first character
        for i in range(rows):
            for j in range(cols):
                # If the first character matches and the word can be found from here, return True
                if board[i][j] == word[0] and search_word(i, j, 0):
                    return True
        # If the word cannot be found, return False
        return False




if __name__ == "__main__":
    row, col = map(int, input().split(" "))
    entries = list(map(str, input().split(" ")))
    grid = np.array(entries).reshape(row, col)
    word1 = input()
    ans1 = search2D(grid, row, col, word)
    print(ans1)


"""
if __name__ == "__main__":
    row, col = map(int, input().split(" "))
    entries = list(map(str, input().split(" ")))
    grid = np.array(entries).reshape(row, col)
    word = input()
    ans1 = search2D(grid, row, col, word)
    print(ans1)
"""






