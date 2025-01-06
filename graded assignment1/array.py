# Prompt the user to input the number of rows
row_num = int(input("Input number of rows: "))

# Prompt the user to input the number of columns
col_num = int(input("Input number of columns: "))

# Create a 2D list (a list of lists) filled with zeros using list comprehension
# The outer list will have 'row_num' elements and the inner lists will have 'col_num' elements
multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

# Nested loop to populate the 2D list with multiplication results
for row in range(row_num):
    for col in range(col_num):
        # Set the value at position [row][col] in the 2D list to the product of 'row' and 'col'
        multi_list[row][col] = row * col
        #print(multi_list)
print(multi_list)

# Print the resulting 2D list containing the multiplication table
#print(multi_list)

import array as arr
a = arr.array('i', [1, 2, 3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(a[i], end=" ")
print()
a.insert(1, 4)
print("Array after insertion : ", end=" ")
for i in (a):
    print(i, end=" ")
print()
b = arr.array('d', [2.5, 3.2, 3.3])
print("Array before insertion : ", end=" ")
for i in range(0, 3):
    print(b[i], end=" ")
print()
b.append(4.4)
print("Array after insertion : ", end=" ")
for i in (b):
    print(i, end=" ")
print()

import array as arr
a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("Access element is: ", a[0])
print("Access element is: ", a[3])
b = arr.array('d', [2.5, 3.2, 3.3])
print("Access element is: ", b[1])
print("Access element is: ", b[2])

import array
arr = array.array('i', [1, 2, 3, 1, 5])
print("The new created array is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\r")
print("The popped element is : ", end="")
print(arr.pop(2))
print("The array after popping is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")

print("\r")
arr.remove(1)
print("The array after removing is : ", end="")
for i in range(0, 3):
    print(arr[i], end=" ")

import array as arr
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr.array('i', l)
print("Initial Array: ")
for i in (a):
    print(i, end=" ")
Sliced_array = a[3:8]
print("\nSlicing elements in a range 3-8: ")
print(Sliced_array)
Sliced_array = a[5:]
print("\nElements sliced from 5th "
      "element till the end: ")
print(Sliced_array)
Sliced_array = a[:]
print("\nPrinting all elements using slice operation: ")
print(Sliced_array)


import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print("The new created array is : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")

print("\r")
print("The index of 1st occurrence of 2 is : ", end="")
print(arr.index(2))
print("The index of 1st occurrence of 1 is : ", end="")
print(arr.index(1))

import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print("Array before updation : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")

print("\r")
arr[2] = 6
print("Array after updation : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")
print()
arr[4] = 8
print("Array after updation : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")



import array
my_array = array.array('i', [1, 2, 3, 4, 2, 5, 2])
count = my_array.count(2)
print("Number of occurrences of 2:", count)

import array
my_array = array.array('i', [1, 2, 3, 4, 5])
print("Original array:", *my_array)
my_array.reverse()
print("Reversed array:", *my_array)

import array as arr

a = arr.array('i', [1, 2, 3, 4, 5])
print("The before array extend  : ", end=" ")
for i in range(0, 5):
    print(a[i], end=" ")

print()
a.extend([6, 7, 8, 9, 10])
print("\nThe array after extend :", end=" ")

for i in range(0, 10):
    print(a[i], end=" ")

print()

import array as arr

a = arr.array('i', [1, 2, 3, 4, 5, 6])
print("The Before extend array is :", end=" ")
for i in range(0, 6):
    print(a[i], end=" ")

print()
a.extend([7, 8, 9, 10, 11, 12])
print("\nThe After extend array is :", end=" ")

for i in range(0, 12):
    print(a[i], end=" ")

print()
b = arr.array('d', [2.1, 2.2, 2.3, 2.4, 2.5, 2.6])

print("\nThe before extend array is :", end=" ")

for i in range(0, 6):
    print(b[i], end=" ")

print()
b.extend([2.6, 2.7, 2.8, 2.9])

print("\nThe after extend array is :", end=" ")

for i in range(0, 9 + 1):
    print(b[i], end=" ")

print()

















