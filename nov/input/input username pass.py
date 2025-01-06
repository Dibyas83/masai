user_name = ["abc","def"]
password = (123,"123")
user = "def"
print(user_name.index(user))

# if password[user_name.index(user)] == int(input("password =",)):
if password[user_name.index(user)] == input("password =",):
    print("logged")
else:print("incorrect")



print(int(input("enter no =")) + 1)

for i in input():

  d = int(i) +1
  print(d)
print()

d =input()
#d =input(),input(),input(),input()
for i in d:
    print(int(i)+1)
print("==============================")

size = int(input())
array =input()
for i in range(size):
  print(int(array[i])+1,end=" ")



N = int(input())
for i in range(N):
    print(int(input()) + 1, end=" ")


d = " "
N = int(input())
for i in range(N):
    d += input()
    print(int(d) + 1, end=" ")


d = " "
N = int(input())
for i in range(N):
    d = input()
    print(int(d) + 1, end=" ")















