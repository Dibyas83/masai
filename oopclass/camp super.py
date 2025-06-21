
# inheriting constructor
# polymerphism has over loading,over riding,operator overloading
class Phone:
    def __init__(self,price,brand,camera,num,place):
        print("inside ph constructor")
        self.price = price
        self.brand = brand
        self.camera = camera
        self.__num = num
        self.place = place
        self.rank = 1


    def buy(self):
        print('buying a ph')
    def get_num(self):
        return  self.__num

class Linux_ph(Phone):
    def __init__(self,price,brand,camera,place,os,ram,num,val):
        super().__init__(price,brand,camera,place,num)
        self.os = os
        self.ram = ram
        self.__val = val
        print("inside linux ph constructor")

    def buy(self): # method over riding feature of polymorphism
        print('buying a linux ph')
        print(self.place)
        print(self.rank)
        super().buy()  # super access only parents method and constructor and not attribute
    def get_val(self):
        return self.__val
ph2 = Linux_ph(100,'apple',20,'bhu','android',4,888,99)
ph2.buy()
print(ph2.brand)
print(ph2.os)
print(ph2.get_num())
print(ph2.get_val())
print(ph2.buy())









