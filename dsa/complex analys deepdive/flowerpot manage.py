# 0 is empty, 1 not . flowers not in adjacent pots.check if n flower can be planted

tc = int(input())
for _ in range(tc):
    m,n = list(map(int,input().split(" ")))
    bed = list(map(int,input().split(" ")))
    count = 0
    i = 0
    while i<m:
        if bed[i] == 0:
            left = (i == 0 or bed[i-1] == 0)
            right = (i == m-1 or bed[i+1])

            if left and right:
                count += 1
                i += 2
            else:
                i+=1
        else:
            i += 1

    if count >= n:
        print("yes")
    else:
        print("no")












