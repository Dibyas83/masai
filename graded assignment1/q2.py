grid=[[1,2],[3,4]]
for row in grid:
    print(row,end=" ")

    for col in row:
        print(col)
    print(col,end=" ")

N=8976
sum = 0
while N > 0:
    sum += N%10
    N=N//10
print(sum)

k = 4
co = 1
i = 1
m = 55
while(i*k <= m):
    co += 1
    m=m-i*k
    i += 1
print(co)

su = 1
x = 4
next_val = x
series = 9
for i in range(1,9):
    if i == 1:
        su += x
    else:
        next_val *= x
        su += next_val
print(su)
















