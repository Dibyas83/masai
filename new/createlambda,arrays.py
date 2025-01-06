# Add 10 to argument a, and return the result:
from functools import reduce

x = lambda a : a + 10
print(x(5))

y = lambda m, n: m * n
print(y(6,7))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

print("--------------55")
data = ["9","8","iou","7","op"]
resul = list(map( lambda x: int(x)* 2 if x.isdigit() else len(x) , data))
print(resul)

nos = [3,4,5,6,7]
resul2 = list(filter(lambda x: x% 2 == 0, map(lambda y:y - 5,nos)))
print(resul2)

words = ["apple","","bana"," ","cher"]
filtered = list(filter(lambda x: x.strip() != "", words))
print(filtered)

nu = [-6,6,0,5,-7,4,7]
res = list(filter(lambda x: x %2 == 0,map(abs,nu)))
print((res))

dat = [(1,2),(5,6),(6,7)]
resu = list(map(lambda x: x[0] + x[1],dat))
print(resu)

stri = ["hollo","tupl","pytthon"]
resut = list(map(lambda s: s[::-1].upper(),filter(lambda x: len(x) > 5,stri)))
print(resut)

n = [4,5,7,22,33]
result2 = reduce(lambda x,y: x if x > y else y,n)
print(result2)

numb = [10,15,20,25,30]
resu2 = list(map(lambda x: x+5 if x%2 == 0 else x-5,filter(lambda y: y>15,numb)))
print(resu2)
print("---------------------------56")
"""

he power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with
an unknown number:

"""

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))


# ---------------------------
cars = ["Ford", "Volvo", "BMW","tata","mercedes"]
x = cars[0]
print(x)
print(cars)
cars[0] = "Toyota"
print(cars)


f= [[[],[]],[[],[]]]

# Print each item in the cars array:

for x in cars:
  print(x)

cars.append("Honda")
# Delete the second element of the cars array:You can also use the remove() method to remove an element from the array.
# e list's remove() method only removes the first occurrence of the specified value.

cars.pop(2)
cars.remove("Volvo")

print(cars)
"""

Method	Description
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

"""










