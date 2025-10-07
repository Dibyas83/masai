

def bonddiasum(matrix,n):
    tot =  0
    tot = sum(matrix[0]) + sum(matrix[n-1])  # 0 and 4 row

    for i in range(1,n-1): # 1-3 row
        tot += matrix[i][0] + matrix[i][n-1]

    for i in range(1,n-1):
        tot += matrix[i][i] + matrix[i][n-i-1]

    if (n%2 == 1):
        tot -= matrix[n//2][n//2]
    print(tot)


"""
1  2  3  4  5 
1  2  3  4  5 
1  2  3  4  5 
1  2  3  4  5 
1  2  3  4  5 

1  2  3  4  5  6
1  2  3  4  5  6
1  2  3  4  5  6
1  2  3  4  5  6
1  2  3  4  5  6
1  2  3  4  5  6


"""




























