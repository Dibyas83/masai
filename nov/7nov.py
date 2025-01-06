class example:
    def __init__(self):
        self.inst_attribute = 2
    @staticmethod  # not instance method ,it cannot access instance variable as it does not use self
    def static_method():
            print("astatic method called")



    def instance_method(self):
        print("instance")
        example.static_method()


# inst.static_method()
obj = example() # calling object
obj.static_method()
obj.instance_method()
inst = example() # calling object

class mydetails:
    classattr = 2

    @classmethod
    def clas_method(cls,newattri):
        cls.classattr = newattri

    def __init__(self,objeample):
        self.obj = objeample

mydetails.clas_method(5)
print(mydetails.classattr)

obj = example()
print(type(obj))

mydetailsobj = mydetails(obj)
mydetailsobj.obj.static_method() # obj = class example
print(mydetails([1,2,3,4]))


class Myclass:
    class_var = 0


    def __init__(self):
        self.instancevar = Myclass.class_var
        Myclass.class_var += 1

a = Myclass()
b = Myclass()
c = Myclass()
print(a.instancevar, b.instancevar ,c.instancevar)
# class_var is 3 now
b=Myclass()
print(b.class_var)
print(b.instancevar)




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



















