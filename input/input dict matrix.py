"""
Below are some of the ways by which we can add user input to a dictionary in Python:

Using a Loop with input() Function
Using Dictionary Comprehension with input() Function
Using update() Method
"""
user_dict = {}

num_entries = int(input("Enter the number of entries you want to add="))

for i in range(num_entries):
    key = input("Enter key")
    value = input("Enter value")
    user_dict[key] = value

print("Dictionary after adding user input", user_dict)

"""
the user is prompted to input the number of dictionary entries they want to add. 
Using a dictionary comprehension, the program then collects key-value pairs from the use
"""


num_entries = int(input("Enter the number of entries you want to add:"))

user_dict = {input(f"Enter key {i+1}:"): input(f"Enter value {i+1}:") for i in range(num_entries)}

print("Dictionary after adding user input:", user_dict)

"""
Through a for loop, key-value pairs are collected from the user, and the `update()` method is
 used to add these pairs to the existing dictionary (`user_dict`).
  Finally, the resulting dictionary is printed
"""
user_dict = {}

num_entries = int(input("Enter the number of entries you want to add:"))

for i in range(num_entries):
    key = input("Enter key:")
    value = input("Enter value:")
    user_dict.update({key: value})

print("Dictionary after adding user input:", user_dict)

"""
Access Dictionary Values Given by User in Python
"""

user_dict = {'name': 'geeks', 'age': 21, 'country': 'India'}
key = input(&quot;Enter a key: &quot;)

value = user_dict[key]
print(f&quot;The value for key '{key}' is: {value}&quot;)



"""
The `get()` method is employed to handle the case where the key is not found,
 providing a default value of "Key not found." The result is then printed.
"""

user_dict = {'name': 'geeks', 'age': 21, 'country': 'India'}
key = input(&quot;Enter a key: &quot;)

value = user_dict.get(key, &quot;Key not found&quot;)
print(f&quot;The value for key '{key}' is: {value}&quot;)

"""
below code prompts the user to input a key and checks if it exists in the dictionary
 `user_dict`. If found, it retrieves and prints the corresponding value;
  otherwise, it notifies the user that the key was not found in the dictionary
"""

user_dict = {'name': 'geeks', 'age': 21, 'country': 'India'}
key = input("Enter a key:")

if key in user_dict.keys():
    value = user_dict[key]
    print(f"The value for key '{key}' is: {value}")
else:
    print(f"Key '{key}' not found in the dictionary.")

"""
he user is prompted to input a key, and a `defaultdict` with a 
default value of "Key not found" is created using the original dictionary `user_dict`. 
The value associated with the entered key is then retrieved from the `default_dict` and printed.
"""

from collections import defaultdict

user_dict ={'name': 'geeks', 'age': 21, 'country': 'India'}
key = input(&quot;Enter a key: &quot;)

default_dict = defaultdict(lambda: &quot;Key not found&quot;, user_dict)
value = default_dict[key]
print(f&quot;The value for key '{key}' is: {value}&quot;)












