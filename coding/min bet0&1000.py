a = 200
b = 45
c = 7
if a&b&c >= 1 & a&b&c <= 1000:

    if a >= b & b >= c:
        print(c)
    elif b >= c & c >= a:
        print(a)
    else:
        print(b)
