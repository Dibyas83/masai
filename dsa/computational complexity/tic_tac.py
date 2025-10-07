
matrix = []
for i in range(3):
    matrix.append(input().split(" "))

for row in matrix:
    if row[0] == row[1] == row[2]:
        print(row[0])
        break
else:
    # check cols
    for col in range(3):
        if matrix[0][col] == matrix[1][col] == matrix[2][col]:
            print(matrix[0][col])
            break
        else:
            if matrix[0][0] == matrix[1][1] == matrix[2][2]:
                print(matrix[0][0])
            elif matrix[0][2] == matrix[1][1] == matrix[2][0]:
                print(matrix[0][2])
            else:
                print("tie")












