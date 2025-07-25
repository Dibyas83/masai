import numpy as np


a1 = [1,2,3,4,5]
b1 = [11,22,33,44,55]
arr1 = np.array(a1)
arr2 = np.array(b1)
arr3 = np.array([3])
arr4 = np.array([1,4,9,16])
g = arr2 - arr1
g2 = arr2 - 2*arr1

#g1 = b1 - a1  unsupported operand type(s) for -: 'list' and 'list'
print(g)
print(g2,"g2")
print(np.subtract(arr2,2*arr1))
print(np.subtract(g2,2*arr1))
print(np.divide(g2,arr1))
print(np.divide(arr2,arr1))
print(np.multiply(arr2,arr1))
print(np.power(arr1,arr3))
print(np.sqrt(arr4))

# combining and splitting array

print(np.concatenate([arr1,arr2]))
print(np.concatenate([arr1,arr2],axis = 0))
conc = np.concatenate([arr1,arr2],axis = 0)
print(conc)
# print(np.concatenate([arr1,arr2],axis = 1))  axis 1 is out of bounds for array of dimension 1
print("-------------------------------")
a11 = [[1,2,3],[4,5,6]]
b11 = [[11,22,33],[44,55,66]]
arr11 = np.array(a11)
arr22 = np.array(b11)
print(np.concatenate([arr11,arr22],axis = 0),"con")
print(np.concatenate([arr11,arr22],axis = 0),"con")
print(np.concatenate([arr11,arr22],axis = 1),"1")
print(np.hstack([arr11,arr22]))
print(np.vstack([arr11,arr22]))

y = np.array_split(conc,3)
z = np.array_split(arr22,3)
print(y)
print(y[1])
print(z)





