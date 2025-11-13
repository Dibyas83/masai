
my_dict = {'b': 2, 'a': 1, 'c': 3}
sorted_items = sorted(my_dict.items())  # Sorts by key by default
sorted_dict_by_key = dict(sorted_items)
print(sorted_dict_by_key)


sorted_items_by_value = sorted(my_dict.items(), key=lambda item: item[1])  # item[0] = key, item[1] = val
sorted_dict_by_value = dict(sorted_items_by_value)
print(sorted_dict_by_value)
print("---------------------")
my_dict = {'apple': 1, 'banana': 2, 'kiwi': 3, 'grape': 4, 'orange': 5}

# Sort the dictionary items (key-value pairs) by the length of the keys
sorted_items = sorted(my_dict.items(), key=lambda item: len(item[0]))

# Convert the sorted list of tuples back into a dictionary (optional)
sorted_dict = dict(sorted_items)

print("Original dictionary:", my_dict)
print("Sorted items by key length:", sorted_items)
print("New dictionary sorted by key length:", sorted_dict)

