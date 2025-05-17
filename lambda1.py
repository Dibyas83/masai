

"""
Python Lambda Functions
Last Updated : 11 Dec, 2024
Python Lambda Functions are anonymous functions means that the function is without a name. As we already know the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python.

In the example, we defined a lambda function(upper) to convert a string to its upper case using upper().




s1 = 'GeeksforGeeks'

s2 = lambda func: func.upper()
print(s2(s1))

Output
GEEKSFORGEEKS
This code defines a lambda function named s2 that takes a string as its argument and converts it to uppercase using the upper() method. It then applies this lambda function to the string ‘GeeksforGeeks’ and prints the result.

Let’s explore Lambda Function in detail:

Python Lambda Function Syntax
Syntax: lambda arguments : expression


lambda: The keyword to define the function.
arguments: A comma-separated list of input parameters (like in a regular function).
expression: A single expression that is evaluated and returned.
Let’s see some of the practical uses of the Python lambda function.

lambda with Condition Checking
A lambda function can include conditions using if statements.

Example:




# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))
print(n(-3))
print(n(0))

Output
Positive
Negative
Zero
Explanation:

The lambda function takes x as input.
It uses nested if-else statements to return “Positive,” “Negative,” or “Zero.”
Difference Between lambda and def Keyword
lambda is concise but less powerful than def when handling complex logic. Let’s take a look at short comparison between the two:

Feature	lambda Function	Regular Function (def)
Definition	Single expression with lambda.	Multiple lines of code.
Name	Anonymous (or named if assigned).	Must have a name.
Statements	Single expression only.	Can include multiple statements.
Documentation	Cannot have a docstring.	Can include docstrings.
Reusability	Best for short, temporary functions.	Better for reusable and complex logic.
Example:




# Using lambda
sq = lambda x: x ** 2
print(sq(3))

# Using def
def sqdef(x):
    return x ** 2
print(sqdef(3))

Output
9
9
As we can see in the above example, both the sq() function and sqdef() function behave the same and as intended.

Lambda with List Comprehension
Combining lambda with list comprehensions enables us to apply transformations to data in a concise way.

Example:




li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

Output
10
20
30
40
Explanation:

The lambda function squares each element.
The list comprehension iterates through li and applies the lambda to each element.
This is ideal for applying transformations to datasets in data preprocessing or manipulation tasks.
Lambda with if-else
lambda functions can incorporate conditional logic directly, allowing us to handle simple decision making within the function.

Example:




# Example: Check if a number is even or odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(4))
print(check(7))

Output
Even
Odd
Explanation:

The lambda checks if a number is divisible by 2 (x % 2 == 0).
Returns “Even” for true and “Odd” otherwise.
This approach is useful for labeling or categorizing values based on simple conditions.
Lambda with Multiple Statements
Lambda functions do not allow multiple statements, however, we can create two lambda functions and then call the other lambda function as a parameter to the first function.

Example:




# Example: Perform addition and multiplication in a single line
calc = lambda x, y: (x + y, x * y)

res = calc(3, 4)
print(res)

Output
(7, 12)
Explanation:

The lambda function performs both addition and multiplication and returns a tuple with both results.
This is useful for scenarios where multiple calculations need to be performed and returned together.
Lambda functions can be used along with built-in functions like filter(), map() and reduce().

Using lambda with filter()
The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True.

Example:




# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

Output
[2, 4, 6]
Explanation:

The lambda function checks if a number is even (x % 2 == 0).
filter() applies this condition to each element in nums.
Using lambda with map()
The map() function in Python takes in a function and a list as an argument. The function is called with a lambda function and a new list is returned which contains all the lambda-modified items returned by that function for each item.

Example:




# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

Output
[2, 4, 6, 8]
Explanation:

The lambda function doubles each number.
map() iterates through a and applies the transformation.
Using lambda with reduce()
The reduce() function in Python takes in a function and a list as an argument. The function is called with a lambda function and an iterable and a new reduced result is returned. This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the functools module.

Example:




from functools import reduce

# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)

#Output24
"""

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica", "Vicky")

x = dict(zip(a, b))
print(x)

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = list(zip(a, b))
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))




