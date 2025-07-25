
"""
1- numpy library is used for scientific and mathematical calculations in python .ex matrix,
fourier analysis,statistics
2- numpy is a package that defines a multidimensional array.array is a datatype that is used
 for calculations.array is not inbuilt in python,it comes with numpy.
3-arrays are not coma separated .it is a collection of items that are stored at contiguous memory
locations.if  20 byte of continous mem address is availabe it will be stored
4-an array can hold fixed no of items,same datatype
5-it is faster ,less mem









"""
import numpy as np

l1 = [11,22,33,44]
l2 = [2,1,4,2]
l3 = [3]
print(l1+l2) # concanate
print(l1*2)
l4 = np.array([11,21,33,44])
same_size = np.array([[11,21,33,44],[22,11,14,12]]) #matrix
# same_sizenot = np.array([[11,21,33,44],[22,11]])
l5 = np.array([22,11,14,12])
l6 = np.array([2])
a=np.array(l1)
b=np.array(l2)
c=np.array(l3)
print(l4)
print(a+b)
print(a*b)
print(a*c)
"""
[11, 22, 33, 44, 2, 1, 4, 2]
[11, 22, 33, 44, 11, 22, 33, 44]
[11 21 33 44]
[13 23 37 46]
[ 22  22 132  88]
[ 33  66  99 132]
"""
st =np.array([2,3,"33"])
fl =np.array([2,3,6.0])
print(st)  # ['2' '3' '33']
print(fl)  # [2. 3. 6.]
#s = np.array([[22,11,14,12],[4]])
#print(s)

slic = np.array([[11, 22, 33, 44, 11, 22, 44],[10, 20, 39, 49, 11, 2, 4]])
print(slic[0:5],"1")
print(slic[3:],"2")
print(slic[0:],"3")
print(slic[0:5,0:5],"4")
print(slic[0:5,0:4],"5")
print(slic[0:5,0:6],"6")
print(slic[3:5,3:5],"7")
print(slic[0,3:5],"8")
print(slic[1,3:5],"9")
print(slic[1,3],"10")

"""
[[11 22 33 44 11 22 44]
 [10 20 39 49 11  2  4]] 1
[] 2
[[11 22 33 44 11 22 44]
 [10 20 39 49 11  2  4]] 3
[[11 22 33 44 11]
 [10 20 39 49 11]] 4
[[11 22 33 44]
 [10 20 39 49]] 5
[[11 22 33 44 11 22]
 [10 20 39 49 11  2]] 6
[] 7
[44 11] 8
[49 11] 9
49 10
"""
print(np.shape(slic))
print(np.size(slic))
print(np.ndim(slic))
print(slic.dtype)
""" 
 (2, 7)
14
2
int64
"""
x = [30,40,50,60,70]
y = [[30,40,50,60,70],[20,30.8,35,48,68]]
arr16 = np.array(x)
arr26 = np.array(y)
print(arr16)
print(arr16.shape)
print(arr26.shape)
print(len(arr26))
print(np.size(arr26))
print(type(arr26),"type") # telling its numpy
print(arr26.dtype,"datatype") #  telling data type
print(arr26.astype(str)) #
print(arr26.astype(float)) #
print(arr26.astype(int)) #
arr26.astype(float)
print(arr26,"float")










