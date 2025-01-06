
"""
Python map() function
Last Updated : 23 Oct, 2024
The map() function is used to apply a given function to every item of an iterable, such as a list or tuple,
 and returns a map object (which is an iterator).

Let’s start with a simple example of using map() to convert a list of strings into a list of integers.

we used the built-in int function to convert each string in the list s into an integer. The map() function
takes care of applying int() to every element
----------------------


-------------







"""
s = ['1', '2', '3', '4']
res = list(map(int, s))
print(res)










def trnsform_arr(arr):
    arr1 = (2, 3, 4, 5, 6)
    max1 = max(arr1)
    result1 = [-1 if x < max1 else x for x in arr1]
    #print(" ".join(result1))
    print(" ".join(map(str , result1)))

d=(3,4,5,6,7)
print(trnsform_arr(d))


"""
map(function, iterable)
Parameter:
function: The function we want to apply to every element of the iterable.
iterable: The iterable whose elements we want to process.


Converting map object to a list
By default, the map() function returns a map object, which is an iterator. In many cases,
 we will need to convert this iterator to a list to work with the results directly.

Example: Let’s see how to double each elements of the given list.
"""

a = [1, 2, 3, 4]

# Using custom function in "function" parameter
# This function is simply doubles the provided number
def double(val):
  return val*2

res = list(map(double, a))
print(res)

print("---------------------------------4")

a = [1, 2, 3, 4]

# Using lambda function in "function" parameter
# to double each number in the list
res = list(map(lambda x: x * 2, a))
print(res)

print("-------------------------5")
a = [1, 2, 3]
b = [4, 5, 6]
res = map(lambda x, y: x + y, a, b)
print(list(res))
print("-------------------------6")

# This example shows how we can use map() to convert a list of strings to uppercase.

fruits = ['apple', 'banana', 'cherry']
res = map(str.upper, fruits)
print(list(res))
print("------------------------7")
# In this example, we use map() to extract the first character from each string in a list.

words = ['apple', 'banana', 'cherry']
res = map(lambda s: s[0], words)
print(list(res))

print("-------------------------------8")
# In this example, We can use map() to remove leading and trailing whitespaces from each string in a list.

s = ['  hello  ', '  world ', ' python  ']
res = map(str.strip, s)
print(list(res))
print("------------------9")

celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))
print("------------------10")


def myfunc(n):
    return len(n)


xy = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(xy))
print("-----------------------11")


def myfunc(a, b):
  return a +"="+ b


wsd = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(wsd))
print("---------------------12")
"""
Method #2: Using string.ascii_lowercase + slicing:
Combination of the above functionalities can also be used to perform this task. In this, 
we use an inbuilt function to get extract the lowercase string and extract the N characters using slicing. 
"""
# Python3 code to demonstrate working of
# Print Alphabets till N
# Using string.ascii_lowercase + slicing
import string

# initialize N
N = 20

# printing N
print("Number of elements required : " + str(N))

# Print Alphabets till N
# Using string.ascii_lowercase + slicing
res = string.ascii_lowercase[:N]

# printing result
print("Alphabets till N are : " + str(res))

print("--------------------------------55")

"""
The Python ord() function converts a character into an integer that represents the Unicode 
code of the character. Similarly, the chr() function converts a Unicode code character into the corresponding string.
"""
# Python3 code to demonstrate working of
# Print Alphabets till N
# Using loop

# initialize N
N = 20

# printing N
print("Number of elements required : " + str(N))

# Print Alphabets till N
# Using loop
s = ""
x = ord('a') + N - 1
y = ord('a')
while (y <= x):
    s += chr(y)
    y += 1

# printing result
print("Alphabets till N are : " + s)

print("----------------------66")

#Python3 code to demonstrate working of
#Print Alphabets till N
#Using list comprehension
#initialize N
N = 20

#printing N
print("Number of elements required : " + str(N))

#Print Alphabets till N
#Using list comprehension
res = ''.join([chr(i) for i in range(ord('a'), ord('a')+N)])

#printing result
print("Alphabets till N are : " + res)
print("--------------------------------")
"""
Method #5: Using recursion

Define a function that takes an integer N as input
If N is less than or equal to 0, return an empty string
If N is greater than 0, recursively call the function with N-1 as input
Convert the ASCII code of the current value of N to its corresponding character using chr() function
Concatenate the character with the result of the recursive call
Return the final result
"""
# Python3 code to demonstrate working of
# Print Alphabets till N
# Using recursion
def print_alphabets(N):

    if N == 0:

        return ''
    else:
        return print_alphabets(N-1) + chr(96+N)

# initialize N
N = 20

# printing N
print("Number of elements required : " + str(N))

# Print Alphabets till N
# Using recursion
res = print_alphabets(N)

# printing result
print("Alphabets till N are : " + str(res))
print("------------------------alpha")
#This code is contributed by Vinay Pinjala.

"""
Method 6: Using the reduce() function from the functools module and string concatenation:

Algorithm:

Initialize the variable N to the desired number of alphabets.
Print the value of N.
Use functools.reduce to iterate over the range of ASCII codes from 97 to 97 + N (where 97 
is the ASCII code for lowercase ‘a’) and concatenate the corresponding characters to the result string.
Print the resulting string of alphabets.
"""
import functools

# initialize N
N = 20

# printing N
print("Number of elements required : " + str(N))

# Print Alphabets till N
# Using reduce
res = functools.reduce(lambda s, i: s + chr(i), range(97, 97+N), '')

# printing result
print("Alphabets till N are : " + str(res))
#This code is contributed by Jyothi Pinjala.

"""

"""
from string import ascii_letters
print([ascii_letters.index(letter) + 1 for letter in ["a", "B", "h", "R"]])














