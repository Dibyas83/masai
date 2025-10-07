x = [1, 2, 3]
y = [4, 5, 6]

for i, j in zip(x, y):
    if i + j > 6:
        break
    print(i * j)
