Dict = {}
t = [(1, 'Geeks'), (2, 'For')]
Dict = dict(t)
print(Dict)

Dict121 = {}
t1 = [(1, 'Geeks'), (2, 'For')]
Dict121 = dict(t1)
print(Dict121)

# Python code to initialize a dictionary
# with only keys from a list

# List of keys
listKeys = ["Paras", "Jain", "Cyware"]

# using zip() function to create a dictionary
# with keys and same length None value
dct = dict(zip(listKeys, [None]*len(listKeys)))

# print dict
print(dct)

