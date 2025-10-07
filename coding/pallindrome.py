n=int(input())
t= n
rev = 0
while n>0:
    dig = n%10
    rev = rev*10 + dig
    n=n//10
if  rev == t:
    print("pal")
else:
    print("not")
    