a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")



i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")


a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(2, 30, 3):
  print(x)

Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")




