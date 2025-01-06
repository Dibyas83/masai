"""
The join() method in Python is used to concatenate the elements of an iterable (such as a list, tuple, or set)
 into a single string with a specified delimiter placed between each element.

separator.join(iterable)


"""
a = ['Hello', 'world', 'from', 'Python']
res = ' '.join(a)
print(res)

# tuple
s = ("Learn", "to", "code")
# Separator "-" is used to join strings
res = "-".join(s)
print(res)

# set
s = {'Python', 'is', 'fun'}
# Separator "-" is used to join strings
res = '-'.join(s)
print(res)


"""
Using join() with Dictionary
When using the join() method with a dictionary, it will only join the keys, not the values. 
This is because join() operates on iterables of strings and the default iteration over a dictionary returns its keys
"""
d = {'Geek': 1, 'for': 2, 'Geeks': 3}

# Separator "_" is used to join keys into a single string
res = '_'.join(d)

print(res)

"""
The join() method takes an iterable (such as a list, tuple, set, or dictionary) and joins its elements 
into a single string using a specified delimiter.


Can the join() method join non-string elements?
No, all elements in the iterable must be strings. If the iterable contains non-string elements, 
they need to be converted to strings first using the str() function.

f the iterable is empty, the join() method returns an empty string without raising any error.
"""













