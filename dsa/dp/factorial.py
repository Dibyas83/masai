
facto = {}
def factorial(n):
    if n in facto:
        return facto[n] # checking if n is already calculated
    if  n == 0:
        return 1
    facto[n] = n * factorial(n-1)
    return facto[n]

print(factorial(5))


#-----------------------

factTable = {}
def factorial1(n):
    try:
        return factTable[n]
    except KeyError:
        if n == 0:
            factTable[0] = 1
            return 1
        else:
            factTable[n] = n * factorial1(n-1)
            return factTable[n]
print(factorial1(5))




