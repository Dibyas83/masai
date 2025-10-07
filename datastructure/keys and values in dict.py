# Python3 code to demonstrate working of
# Ways to extract all dictionary values
# Using values()

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extracting all dictionary values
# Using values()
res = list(test_dict.values())

# printing result
print("The list of values is : " + str(res))


# Python3 code to demonstrate working of
# Ways to extract all dictionary values
# Using list comprehension

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extracting all dictionary values
# Using list comprehension
res = [val for val in test_dict.values()]

# printing result
print("The list of values is : " + str(res))








