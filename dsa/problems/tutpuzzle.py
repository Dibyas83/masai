def find_grid(matrix, input_str, row_pos, col_pos, row_count, col_count, degree) :
   if degree == len(input_str):
      return True
   if row_pos < 0 or col_pos < 0 or row_pos >= row_count or col_pos >= col_count :
      return False
   if matrix[row_pos][col_pos] == input_str[degree] :
      temp = matrix[row_pos][col_pos]
      matrix[row_pos].replace(matrix[row_pos][col_pos], "#")
      result = (find_grid(matrix, input_str, row_pos - 1, col_pos, row_count, col_count, degree + 1) |find_grid(matrix, input_str, row_pos + 1, col_pos, row_count, col_count, degree + 1) |find_grid(matrix, input_str, row_pos, col_pos - 1, row_count, col_count, degree + 1) |find_grid(matrix, input_str, row_pos, col_pos + 1, row_count, col_count, degree + 1))
      matrix[row_pos].replace(matrix[row_pos][col_pos], temp)
      return result
   else :
      return False
def solve(matrix, input_str, row_count, col_count) :
   if len(input_str) > row_count * col_count:
      return False
   for row in range(row_count) :
      for col in range(col_count) :
         if matrix[row][col] == input_str[0] :
            if find_grid(matrix, input_str, row, col, row_count, col_count, 0):
               return True
   return False
row, col = map(int, input().split(" "))
grid = []
for _ in range(row):
    entries = list(map(str, input().split(" ")))
    grid.append(entries)
word = input()
print(solve(grid, word, row, col))

"""
if __name__ == "__main__":
    row, col = map(int, input().split(" "))
    entries = list(map(str, input().split(" ")))
    grid = np.array(entries).reshape(row, col)
    word = input()
    ans1 = search2D(grid, row, col, word)
    print(ans1)
"""








