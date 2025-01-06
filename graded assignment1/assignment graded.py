def Solve(N):
  if N%4 == 0 and N%6 == 0:
    print("Awesome!")
  elif N%4 == 0:
    print("Four!")
  elif N%6 == 0:
    print("Six!")
  else:
    print("Dark!")


def sum_of_even_numbers(num):
  total = 0
  for i in range(1,num+1):
    if i%2 == 0:
      total += i
  print(total)



arr=[1,7,3,4,5]
max = arr[0]
for i in range(0,len(arr)):
    if(arr[i] > max):
      max = arr[i]
print("max is" + str(max))

n=int(input("no is="))
for i in range(1,n+1):
  if n%i == 0:
    print(i,end=" ")

n=int(input("no is="))
su = 0
for i in range(1, n + 1):
  if n % i == 0:
    su = su + i
print("sum is=", su)

def find_divisors(n):
  for i in range(1,n+1):
    if n%i == 0:
      print(i,end=" ")

A=44
B=33
C=22
if A > C:
  if B > C:
    print("AC")
  else:
    print("No AC")
elif C > A:

  if B > A:
    print("AC")
  else:
    print("No AC")
else:
  print("No AC")

n = 120
m = 0
if n%10 < 0:
  print(n)
while n%10 >=0:
  if n%10 >= m:
    m = n%10
  n = n//10
print(m)

n = 4
m = 0
while n > 0:
    f = n%10
    if f >= m:
        m = f
    n = n//10
print(m)




