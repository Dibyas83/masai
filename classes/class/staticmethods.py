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