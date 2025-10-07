




a =(1,4,7,4,6) # tuple
# a[1] = 9  cnnot be changed
print(a)
list(a)
b = list(a)
b.append(44)
a=tuple(b)
print(list(a))
print(b)
print(a)
print(tuple(b))
frit11 =("ab","cd","ef")
(ee,bb,cc) = frit11
print(ee)
print(bb)
print(cc)
print("-----------------------")

# dictionaries
person = {"name":"alice","age":24}
print(person["name"])

a1 =2,3,5 # comma is compulsory
f = ("abc",)
print(a)
b = (4)
c = [1,2,4,6,4]
c1 = list((1,2,4,6,4))
c1.remove(4)
c1.pop(3)
c += [4,5]
print(type(a))
print(type(b))
print(type(c))
print(type(c1))
print(c1)

result = a + a1*2
print(result)

dict1 = {"a":1,"b":6,"ui":8}
dict1.update({"year":2020})
dict1["years"] = 2090
gh =dict1.get("b")
kk = dict1.keys()
kv = dict1.values()
ki = dict1.items()
print(kk)
print(kv)
print(gh)
print("----------------------------------66")
print(dict1)
for item in dict1:
    print(item,end=" ")
    print(dict1[item])

print("=========================1")
dict1["a"] =6
print(dict1)
print(dict1.popitem())
print(dict1.popitem())

set1 = {"red","yel","uyt"}
set2 = {"tyu","red","uyt"}
set2.add("fg")
set2.update(set1)
s3 = set1.union(set2)
s4 = set1 | set2
s = {3,4,5,7,6}
s2 = {5,7,8,3}
result2 = set1 & set2 # no slicing
r = s & s2 | s2-s
r2 = s & s2 | s-s2
print(result2)
print(r)
print(r2)
print(set2)
print(s3)
print(s4)



















