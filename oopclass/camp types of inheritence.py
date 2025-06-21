



"""
single level inh - 1 parent 1 child
multi level inh - grandparent > parent > child each inheriting the above
hierarchical inh- many parents,many child  ex courses - students in udemy
multiple inh - father,mother to child

"""
# ex multiple inh

class Phone:
    def __init__(self,price,brand,camera):
        print('inside phone')
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print('buying a ph')

    def retun_ph(self):
        print('returning')

class Product:

    def __init__(self,price,type,rating):
        print('inside product')
        self.__price = price
        self.type = type
        self.rating = rating

    def buy(self):
        print('buying a product')

    def review(self):
        print('*****')

class Smartphone(Product,Phone): # method resolution order
    pass

s= Smartphone(1000,'sams',5)

s.buy()
s.review()
print('------------------------------')

class A:

    def m(self):
        return 20


class B(A):

    def m(self):
        return 30
    def n(self):
        return 40

class C(B):

    def n(self):
        return 50

obj1 = A()
obj2 = B()
obj3 = C()
print(obj1.m() + obj3.m() + obj3.n()) # 20 + 30 + 50





