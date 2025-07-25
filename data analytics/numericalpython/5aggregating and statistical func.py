
import numpy as np
import statistics as st


a1 = [1,2,2,4,5]
b1 = [11,22,33,44,55]
a11 = [[1,2],[3,4]]
b11 = [[11,22],[44,55]]


arr1 = np.array(a1)
arr11 = np.array(a11)
arr2 = np.array(b1)
arr22 = np.array(b11)

print(np.sum(arr1))
print(np.min(arr1))
print(np.max(arr1))
print(np.size(arr1))
print(np.mean(arr1))
print(np.cumsum(arr1))  # cumulative sum
print(np.cumprod(arr1))  # cumulative product
# print(np.count(arr1))

price = arr1
quant = arr2
print(price,"\n",quant)
print(np.sum(price))
print(np.cumsum([price,quant],axis = 0))  # preice *quant
print(np.cumprod([price,quant],axis = 0))  # preice *quant
cumu = np.cumprod([price,quant],axis = 0) # preice *quant

print(cumu[1].sum()) # sum of row 1

# statistical fuctions
baked_food = arr1
print(np.mean(baked_food))
print(np.median(baked_food)) # sort then centre value , if even then avg
print(st.mode(baked_food)) # max accurence
print(np.std(baked_food)) # standard deviation
print(np.var(baked_food)) # standard deviation ** 2

wine_cons_cities = [20,30,10,60,50,80]
death = [4,6,2,8,7,11]
print(np.corrcoef([wine_cons_cities,death]))  # correlation of- -1 represents inv proportional,
# direct propertional,0 no rela

price1 = [300,150,200,100,350]
sales = [20,40,25,40,10]
print(np.corrcoef([price,sales]))