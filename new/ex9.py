


def calculate_expression(a,b,c,d,e,f):
    sum1 = 0
    sum2 = 0
    sum3 = 0

    for letter in (a,b,c,d,e,f):
        sum1 += letter #sums all
        print(sum1)
        if letter == d:
            pass
        else:
            sum2 += letter  # gives sum of a,b,c
    sum3=sum2 * sum1
    print(sum3)

















