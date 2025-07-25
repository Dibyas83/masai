
import numpy as np

a1 = [11,2,33,4,5,1]
b1 = [11,22,33,44,55]
a11 = [[1,2],[3,4]]
b11 = [[11,33,22],[66,44,55]]


arr1 = np.array(a1)
arr11 = np.array(a11)
arr2 = np.array(b1)
arr22 = np.array(b11)
arr3 = np.array([3])
arr4 = np.array([1,4,9,16])

c1 = np.concatenate([arr11,arr22],axis = 1)

print(np.sort(arr1))
pr= np.sort(arr1)

p= np.sort(b11)
print(type(p))
s = np.where(arr1 == 4)
s1 = np.where(arr1 % 2 == 0)
s2 = np.searchsorted(pr,2) # works on sorted single dimensional array
s3 = np.searchsorted(pr,1)
s4 = np.searchsorted(pr,4)
s5 = np.searchsorted(pr,5)
s6 = np.searchsorted(pr,33)
print(s)
print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(s6)

fa = [False,True,True,False,True,False]  # filters the true
new = pr[fa]
print(new)

fi = pr > 35
new1 = pr[fi]
print(new1)

fo = pr % 2 == 0
new2 = pr[fo]
print(new2)

