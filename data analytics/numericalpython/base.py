

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

