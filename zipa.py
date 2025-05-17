
"""
zip() in Python
Last Updated : 30 Dec, 2024
The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples. Each tuple contains elements from the input iterables that are at the same position.

Let’s consider an example where we need to pair student names with their test scores:




names = ['John', 'Alice', 'Bob', 'Lucy']
scores = [85, 90, 78, 92]

res = zip(names, scores)
print(list(res))

Output
[('John', 85), ('Alice', 90), ('Bob', 78), ('Lucy', 92)]
Explanation:

zip() is used to combine the two lists into a single iterable ‘res‘
Each element from names is paired with the corresponding element from scores
list() converts the iterator from zip() into a list of tuples, making it easier to visualize or manipulate the combined data.
Table of Content

Syntax of zip()
Examples of zip()
Iterables of different Lengths
Unzipping data with zip()
Combine dictionary keys and values
Syntax of zip()
zip(*iterables)


Parameters:
*iterables refers to one or more iterable objects (like lists, tuples, etc.) that we want to combine. The function pairs elements from these iterables into tuples based on their positions.

Return value:
Returns an iterator of tuples, where each tuple contains elements from the input iterables at the same index. If the input iterables are of unequal length then zip() stops creating tuples when the shortest iterable is exhausted.

Key Points:

If no parameters are passed, zip() returns an empty iterator.
If only one iterable is passed, the result will be a series of single-element tuples.
If multiple iterables are passed, each tuple will contain one element from each iterable.
Examples of zip()
Below example shows how zip() works when no parameter, one and two iterable are passed into parameter.




a = [1, 2, 3]
b = ['a', 'b', 'c']

# No iterable are passed
res = zip()

# Converting iterator to list
print(list(res))

# One iterable is passed
res = zip(a)

# Converting iterator to list
print(list(res))

# Two iterables are passed
res = zip(a, b)

# Converting iterator to list
print(list(res))

Output
[]
[(1,), (2,), (3,)]
[(1, 'a'), (2, 'b'), (3, 'c')]
Iterables of different Lengths
When using iterables of different lengths, the zip() will only pair up to the shortest iterable.




names = ['Alice', 'Bob', 'Charlie']
scores = [88, 94]

res = zip(names, scores)
print(list(res))

Output
[('Alice', 88), ('Bob', 94)]
Explanation: Here, zip() stops after pairing the two available score values with the first two name values. ‘Charlie’ is left out since there’s no corresponding score value.

Unzipping data with zip()
We can also reverse the operation by unzipping the data using the * operator. Let’s see how that works:




a = [('Apple', 10), ('Banana', 20), ('Orange', 30)]

fruits, quantities = zip(*a)

print(f"Fruits: {fruits}")
print(f"Quantities: {quantities}")

Output
Fruits: ('Apple', 'Banana', 'Orange')
Quantities: (10, 20, 30)
Explanation: Using the * operator, we can separates (unzip) the paired fruit names and their quantities back into their respective sequences

Combine dictionary keys and values
We can use zip() to combine dictionary keys and values, or even iterate over multiple dictionaries simultaneously. Here’s an example pairing dictionary keys and values.




d = {'name': 'Alice', 'age': 25, 'grade': 'A'}

keys = d.keys()
values = d.values()

res = zip(keys, values)
print(list(res))

Output
[('name', 'Alice'), ('age', 25), ('grade', 'A')]

"""










