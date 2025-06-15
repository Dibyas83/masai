
"""
The count() function in Python is a built-in method used to count the number of occurrences of a specific element within a sequence, such as a string, list, or tuple. It returns an integer representing the number of times the specified element appears in the sequence. If the element is not found, it returns 0.
Python

string = "hello world"
count_l = string.count("l")
print(count_l)  # Output: 3

list_numbers = [1, 2, 2, 3, 2, 4]
count_2 = list_numbers.count(2)
print(count_2)  # Output: 3

tuple_vowels = ('a', 'e', 'i', 'o', 'u', 'a')
count_a = tuple_vowels.count('a')
print(count_a) # Output: 2
The count() function can also take optional start and end arguments to specify a range within the sequence to search.
Python

string = "hello world hello"
count_hello = string.count("hello", 0, 11)
print(count_hello) # Output: 1
In this case it will only search from index 0 to 10, so the second "hello" will not be counted.
"""










