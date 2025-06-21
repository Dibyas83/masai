
# inheriting constructor
# polymerphism has over loading,over riding,operator overloading
class Phone:
    def __init__(self,price,brand,camera,no):
        print("inside ph constructor")
        self.price = price
        self.__brand = brand
        self.camera = camera
        self.__no = no

    def get_no(self):
        return self.__no

    def buy(self):
        print('buying a ph')

    def return_ph(self):
        print('damaged')

class Linux_ph(Phone):

    def __init__(self,val,no): # since i have constructor i cannot use Phone constructor
        self.__val = val

    def get_val(self):
        return self.__val

    def buy(self): # method over riding feature of polymorphism
        print('buying a linux ph')

    def enroll(self):
        print('enroll')

    def review(self):
        print('revw')

class Android_ph(Phone):
    def course(self):
        print('subject')
    def account(self):
        print('transactions')

ph1 = Android_ph(20000,'apple',13,100)  #will inherit phone constructor
ph2 = Linux_ph(100,20)

#print(ph2.get_no()) # can not use parent constructor
#print(ph1.__brand)  private attribute of Phone
print(ph1.price)
#print(ph1.__no)
print(ph1.get_no())










