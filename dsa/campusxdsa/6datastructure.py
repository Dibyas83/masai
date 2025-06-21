
# balancing time and space -different problems require different logical structure

"""
1 - to add a file browser feature in operating system.loops and recursion can do it but tree is best

2 - to implement a friend suggestion function in social networking app ,using graph is most efficient

3 - if in a website like google  ,when using "go back" button stack is most efficient using lifo

4 for adding a feature of undo and redo in text editor ,stack is best


        LINEAR DS - array,linked list, stacks , queue , hashing
DS
        NON LINEAR - tree,graph
------------------------------
array =data same type,mem address continuos,so only need to know first address and  size
its size is (static)fixed,mem wastage if not used fully.
we can use referential arrays to make data stored in it heterogeneous(different data types) by storing data in different mem locations and store adresses of mem loc in array instead of data also called as call by refference
but its speed dec and more memory is used
to make array size dynamic  we use dynamic array
[] - static
[     ] - new double size array according to need created and data copied
python list is an dynamic array

"""
#from matrixa import result

"""
lets create a class list and add functions like len,append,print,indexing,pop,clear,find,insert,delete,remove
sort/min/max/sum/extend/negetive indexing,slicing,merge

ctypes is a foreign function library for Python. It provides C-compatible data types and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python. 
Key features of ctypes:
C-compatible data types:
ctypes provides data types that correspond to C data types, such as c_int, c_float, c_char_p, etc.
Calling functions in shared libraries:
You can load shared libraries (.dll on Windows, .so on Linux, .dylib on macOS) and call functions within them using ctypes.
Wrapping libraries in pure Python:
ctypes allows you to create Python wrappers around C libraries without writing any C code.
How to use ctypes:
Import the ctypes module.


import ctypes
lib = ctypes.cdll('my_library.dll') #Load the shared library: Use ctypes.CDLL (or ctypes.windll or ctypes.oledll
# on Windows) to load the library.
my_function = lib.my_function  #Access functions from the library: Access the functions within the library
# as attributes of the loaded library object.
my_function.argtypes = [ctypes.c_int, ctypes.c_char_p] #Specify the argument types: Set the argtypes attribute of
# the function object to specify the expected argument types.

my_function.restype = ctypes.c_int  #Specify the return type: Set the restype attribute of the function object
# to specify the return type.

result = my_function(10, b"hello")  #Call the function: Call the function like a regular Python function.


Example:
Let's say you have a C function in a shared library called my_library.so (or my_library.dll on Windows):
C

// my_library.c
#include <stdio.h>

int add(int a, int b) {
    return a + b;
}
To compile this, use:
Code

gcc -shared -o my_library.so -fPIC my_library.c # Linux
gcc -shared -o my_library.dll my_library.c # Windows
Here's how to call it from Python using ctypes:
Python



# Access the function
add_func = lib.add

# Specify argument and return types
add_func.argtypes = [ctypes.c_int, ctypes.c_int]
add_func.restype = ctypes.c_int

# Call the function
result2 = add_func(5, 3)
print(result2) # Output: 8

Important considerations:
Data type conversion:
Be mindful of data type conversions between Python and C. ctypes provides tools for this, but incorrect types can lead to errors.
Memory management:
When working with pointers, pay close attention to memory management. Python's automatic garbage collection doesn't apply to C memory, so you need to manage it manually, if needed.
Error handling:
C functions can raise errors that Python might not catch. Check the documentation of the C library to understand how to handle errors.
Platform compatibility:
Shared library names and paths can be platform-dependent.
Callback functions:
ctypes allows creation of C callable function pointers from Python callables. 
Structures:
The ctypes.Structure class can be used to create Python representations of C structs.
"""
# dynamic arrays
import ctypes

class Meralist:

    def __init__(self):
        self.size = 1   # variable size = capacity of array
        self.n = 0      # variable n = no of items in array currently
        # create a ctype array with size = self.size
        self.a = self.__make_array(self.size)#  a func created to create array giving self.size as input

    def __len__(self):
        return  self.n

    def __str__(self):    # to print
        res = ' '
        for i in range(self.n):
            res = res + str(self.a[i]) + ','

        return '[' + res[:-1] + ']'

    def __getitem__(self, index):
        if 0 <= index < self.n:
            return self.a[index]
        else:
            return 'Indexerror'

    def __delitem__(self, pos): # shifting to left direction
        if 0 <= pos < self.n:
            for i in range(pos, self.n - 1):
                self.a[i] = self.a[i + 1]  # i = pos

        self.n = self.n - 1

    def append(self,item):
        if self.n == self.size: # resize
            self.__resize(self.size*2)

        # append if there space
        self.a[self.n] = item
        self.n = self.n + 1 # inc size after every item added

    def pop(self):
        if self.n == 0:
            return 'empty'
        print(self.a[self.n -1])
        self.n = self.n -1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.a[i] == item:
                return i
        return 'ValueError'

    # to insert list size increases and shifting is done from end to the position where it is to be inserted
    # , for which a loop is run in rev and a[5] = a[4] is done lastly a[2] = 100 new iteem at pos 3,then inc size of array n= n+1
    def insert(self,pos,item):
        if 0 <= pos < self.n:
            if self.n == self.size:
                self.__resize(self.size * 2)

            for i in range(self.n, pos, -1):
                self.a[i] = self.a[i - 1]

            self.a[pos] = item
            self.n = self.n + 1

        else:
            return 'indexerror'

    def remove(self,item): # search the item ,del ad shift left
        pos = self.find(item)

        if type(pos) == int:
            self.__delitem__(pos)
        else:
            return pos


    def __resize(self,new_capacity):
        b = self.__make_array(new_capacity)  # create  a new array with new capacity
        self.size = new_capacity
        for i in range(self.n): # copy the content of a to B
            b[i] = self.a[i]
        self.a = b # reasign a


    # create list
    def __make_array(self,capacity):
        return (capacity*ctypes.py_object)()   #this is a c code,it returns ctype array(static whose size is told before creation and it is also referential) with size capacity


l = Meralist()
print(type(l)) # l is a object mem address
l.append('hello')
l.append(4)
l.append(True)
l.append(6)
print(l)
print(l[3])
print(l[5])
print(l.pop())
print(l)
l.insert(2,8)
l.insert(4,11)
print(l)








