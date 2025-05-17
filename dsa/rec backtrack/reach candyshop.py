
def find_longest_path(matrix, start_row, start_col, end_row, end_col):
  """
  Finds the maximum length path from a start cell to an end cell in a binary matrix.
  The matrix is a 2D list of 0s (obstacles) and 1s (free paths).
  The algorithm uses DFS and backtracking to explore all possible paths.
  The function returns the length of the longest path found.
  """

  if not matrix or not matrix[0]:
    return -1  # Invalid matrix

  rows = len(matrix)
  cols = len(matrix[0])

  if start_row < 0 or start_row >= rows or start_col < 0 or start_col >= cols or \
     end_row < 0 or end_row >= rows or end_col < 0 or end_col >= cols or \
     matrix[start_row][start_col] == 0 or matrix[end_row][end_col] == 0:
    return -1  # Invalid start or end cell

  max_path_length = 0

  def dfs(row, col, current_path_length, visited):
    nonlocal max_path_length

    # Base cases:
    # 1. Reached the destination
    if row == end_row and col == end_col:
      max_path_length = max(max_path_length, current_path_length)
      return

    # 2. Invalid cell or already visited
    if row < 0 or row >= rows or col < 0 or col >= cols or \
       matrix[row][col] == 0 or (row, col) in visited:
      return

    # Explore all 4 directions:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for dr, dc in directions:
      new_row, new_col = row + dr, col + dc
      dfs(new_row, new_col, current_path_length + 1, visited | {(row, col)})  # Add current cell to visited

  # Start DFS from the start cell
  dfs(start_row, start_col, 1, set())

  return max_path_length





