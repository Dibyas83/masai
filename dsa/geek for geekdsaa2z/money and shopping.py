
def get_min_price(shops,shop_n):
    for i in range(1,shop_n): # shops  visited in row,
        shops[i][0] += min(shops[i-1][1],shops[i-1][2])
        print(shops[i][0])
        shops[i][1] += min(shops[i-1][0],shops[i-1][2])
        print(shops[i][1])
        shops[i][2] += min(shops[i-1][0],shops[i-1][1])
        print(shops[i][2])
        print(shops)
    return min(shops[shop_n-1][0],shops[shop_n-1][1],shops[shop_n-1][2])

for _ in range(int(input())): # test cases
    no_of_shops = int(input()) # shop_n
    arr = [list(map(int,input().split(" "))) for i in range(no_of_shops)]
    print(arr)
    print(get_min_price(arr,no_of_shops))

"""
1
5
2 3 4
3 2 5
5 2 3
6 4 3
5 6 2
arr or shops = [[2, 3, 4], [3, 2, 5], [5, 2, 3], [6, 4, 3], [5, 6, 2]]
calculation starts from 2nd shop
3+3 = 6
2+2 =4
 5+2 =7
[[2, 3, 4], [6, 4, 7], [5, 2, 3], [6, 4, 3], [5, 6, 2]]
9
8
7
[[2, 3, 4], [6, 4, 7], [9, 8, 7], [6, 4, 3], [5, 6, 2]]
13
11
11
[[2, 3, 4], [6, 4, 7], [9, 8, 7], [13, 11, 11], [5, 6, 2]]
16
17
13
[[2, 3, 4], [6, 4, 7], [9, 8, 7], [13, 11, 11], [16, 17, 13]]
13

"""






