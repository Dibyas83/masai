
def calculate_expression(a,b,c,d,e,f):
    a = 2
    b = 4
    c = 5
    d = 3
    e = 2
    f = 7
    sum1 = 0
    sum2 = 0
    sum3 = 0
    for letter in (a,b,c,d,e,f):
        sum1 += letter
        if letter == d:
            pass
        else:
            sum2 += letter
    print("sum2=",sum2)