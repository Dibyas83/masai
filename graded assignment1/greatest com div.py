# greatest common divisor 36 and 48 ,12 is gcd
num1 =15
num2 = 10
result = 1
if num1 <= num2:
    for i in range(1,num1+1):
        if num1%i == 0 and num2%i == 0:
            result = i
else:
    for i in range(1,num2+1):
        if num1%i == 0 and num2%i == 0:
            result = i
    #return result
    print(result)
