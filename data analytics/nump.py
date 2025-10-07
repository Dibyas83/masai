
li = [1,2,3,4]
li = li * 5
print(li)

import numpy

lii = [1,2,3,4,5]
lii = numpy.array(lii) # numpy.array(lii)
print(lii,type(lii))
lii = lii * 5
print(lii)

lii2 = [3,4,5,6,7]
lii3 = [3,4,5,6,7]
print(lii2+lii3)
print(lii2+lii)  # lii is already numpy

print(numpy.array(lii3) + numpy.array(lii2))

list1 = []
for i in range(len(lii3)):
    list1.append(lii3[i] + lii2[i])

import numpy as np

print(np.array([1,2,3]))
print(np.zeros((2,2)))
print(np.arange(5)) # can use floating point value
print(list(np.arange(5))) # can use floating point value
print(list(numpy.arange(1,5.5,0.5)))#print(f)
print(list(np.arange(1,5.5,0.5)))#print(f)
print(np.arange(1, 5.5,0.5))#print(f)
arr1 = np.array([10,20,30])
print(arr1)

l4 = []
for i in list1:
    l4.append(i*2)
print(l4)


a = numpy.ones((3,3))
b = a + [3,4,5]
print(b)
print(numpy.max(b,axis = 0)) # max o each col
print(numpy.max(b,axis = 1)) # max of row
print(numpy.max(b))

n = np.zeros((3,3))
n[1,1] = 1
print(n)
kk = np.sum(b)
kk1 = np.max(b)
kk11 = np.max(b,axis = 0)
kk12 = np.max(b,axis=1) # max of row
kk2 = np.mean(b)
print(kk,kk1,kk2)
print(kk11,kk12)














