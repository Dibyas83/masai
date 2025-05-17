
"""


def binconv(n):

    arr = [128,64,32,16,8,4,2,1]
    if n == 1:
        return arr[-1] = 1
    if n >= 128:
        return arr[0] = 1
        n = n - 128
    if n >= 64:
        return arr[1] = 1
        n = n - 64
    if n >= 32:
        return arr[2] = 1
        n = n-32
    if n >= 16:
        return arr[3] = 1
        n= n-16
    if n >= 8:
        return arr[4] = 1
        n =n-8
    if n >= 4:
        return arr[5] = 1
        n =n-4
    if n >= 2:
        return arr[6] = 1
        n = n-2
    if n == 1:
        return arr[7] = 1
        n = n-1
    else:


   # return bin[i] =1 if (x- arr[n-1-i]) > 0

"""
def binary(n):
    if n == 0:
        return ""
    return binary(n//2) + str(n%2)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(binary(n))

if __name__== "__main__":
    main()

# print(1%2)  == 1
# print(1//2) == 0

