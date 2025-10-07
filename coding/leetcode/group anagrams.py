
"""
- You can create a hashmap (dictionary) in Python using either curly braces {} or the dict() constructor.
create a dict with sorted str in keys and all original words in a list as values

taking string as key and list as values we create hashmap
add  same words to values
create two list one with original ,one with sorted
create a dict with string as key and empty list as values

"""
def groupana(stri):
    stri2 = []
    ans = []

    for i in range(len(stri)):
        stri2.append("".join(sorted(stri[i])))
    print(stri)
    print(stri2)

    dict1 = {}
    for i in range(len(stri2)):
        dict1[stri2[i]] = []

    for i in range(len(stri)):
        dict1[stri2[i]].append(stri[i])

    print(dict1)
    for value in dict1.values():
        ans.append(value)

    return ans

stri = list(map(str,input().split(" ")))
print(groupana(stri))
"""

        
my_dict = {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}
my_dict['fruits'].append('orange')
print(my_dict)


my_string = "hello"

# Sort the string
sorted_characters = sorted(my_string)
sorted_string = "".join(sorted_characters)

print(sorted_string)


The sorted() function returns a new sorted list without modifying the original list.

my_list = ["banana", "apple", "cherry", "date"]
sorted_list = sorted(my_list)
print(sorted_list)

The list.sort() method sorts the list in-place, meaning it modifies the original list and returns None
my_list = ["banana", "apple", "cherry", "date"]
my_list.sort()
print(my_list)

        my_list = ["banana", "apple", "cherry"]
        sorted_list_desc = sorted(my_list, reverse=True)
        print(sorted_list_desc)

        my_list = ["Banana", "apple", "Cherry"]
        sorted_list_case_insensitive = sorted(my_list, key=str.casefold)
        print(sorted_list_case_insensitive)

        my_list = ["apple", "banana", "cherry"]
        sorted_by_length = sorted(my_list, key=len)
        print(sorted_by_length)

Sorting by a specific part of the string (e.g., a number in the string):
Python

        import re

        data = ['data_page10of10.png', 'data_page1of10.png', 'data_page2of10.png']
        sorted_data = sorted(data, key=lambda x: int(re.search(r'\d+', x).group()))
        print(sorted_data)

---------------------------

# Creating an empty hashmap

my_hashmap = {} 
or
my_hashmap = dict() 

# Creating a hashmap with initial key-value pairs
fruit_prices = {"apple": 1.50, "banana": 0.75, "orange": 1.20}

# Creating a hashmap from a list of tuples
student_grades = dict([("Alice", "A"), ("Bob", "B"), ("Charlie", "C")])

# Creating a hashmap using keyword arguments
person_info = dict(name="John Doe", age=30, city="New York")
"""