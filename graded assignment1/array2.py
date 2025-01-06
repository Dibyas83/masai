import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
largest = a[0]
for i in range(1, len(a)):
   if a[i]>largest:
      largest=a[i]
print ("Largest number:", largest)



import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
b = arr.array('i')
for i in range(len(a)):
   if a[i]%2 == 0:
      b.append(a[i])
print ("Even numbers:", b)



import array as arr
a = arr.array('i', [10,5,15,4,6,20,9])
print (a)
s = 0
for i in range(len(a)):
   s+=a[i]
avg = s/len(a)
print ("Average:", avg)

# Using sum() function
avg = sum(a)/len(a)
print ("Average:", avg)






































