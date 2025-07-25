
import numpy as np

a1 = [1,2,3,4,5]
b1 = [11,22,33,44,55]
a11 = [[1,2],[3,4]]
b11 = [[11,22],[44,55]]


arr1 = np.array(a1)
arr11 = np.array(a11)
arr2 = np.array(b1)
arr22 = np.array(b11)
arr3 = np.array([3])
arr4 = np.array([1,4,9,16])

c1 = np.concatenate([arr11,arr22],axis = 1)
print(np.concatenate([arr11,arr22],axis = 1),"1")
print(c1,"c1")
x = np.append(arr2,[12,14])
print(x.dtype)
print(type(x))
print(x)
print(np.insert(x,2,455))
print(np.insert(c1,2,[15,4,6,7],axis = 0))
print(np.insert(c1,2,[77],axis = 0))
print(np.insert(c1,[1,2],[77],axis = 0)) # on both 1 and 2 indexex
print(c1,"c12")
print(np.delete(c1,2),"delete")
print(np.delete(c1,[2,5]),"delete")

print(np.delete(c1,1,axis = 1),"delete")
print(np.delete(c1,[1],axis = 1),"delete")
print(c1,"c13")
"""
[[ 1  2 11 22]
 [ 3  4 44 55]] 1
[[ 1  2 11 22]
 [ 3  4 44 55]] c1
int64
<class 'numpy.ndarray'>
[11 22 33 44 55 12 14]
[ 11  22 455  33  44  55  12  14]
[[ 1  2 11 22]
 [ 3  4 44 55]
 [15  4  6  7]]
[[ 1  2 11 22]
 [ 3  4 44 55]
 [77 77 77 77]]
"""





