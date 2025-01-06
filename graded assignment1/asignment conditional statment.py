"""
According to the definition of prime numbers, any whole number which has only 2 factors is
 known as a prime number. Now, the factors of 2 are 1 and 2. Since there are exactly two factors of 2,
"""
num = 23

pri = 1
rev_no = 0
if num == 1:
    print("No")
for i in range(2, num):
    if num % i == 0:
        print("No")
        break

else:
    pri = num
    print("prime")

p = len(str(pri))
for j in range(1,p+1):
    rem = (pri%10) # 1  ,0
    pri = (pri - rem)//10 # 101-1//10 = 10, 10//10=1
    rev_no += rem*10**(p-j)

print(rev_no)
for i in range(2, rev_no):
    if rev_no % i == 0:
        print("No")
        break
    else:
        print("Yes")
        break




