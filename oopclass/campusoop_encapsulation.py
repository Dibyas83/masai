

# instance variables are declared inside a special method called _init_ which has input called self

# value of instance var are different for different objects
# for every data member we can create 2 functions ,getter and setter after markin as private (__)
# to make it able to be seen create a func and a func to change the data
class Atm:
    def __init__(self):  # constructor is a method ,the codes inside it is automatically executed when we create a object of this class
        self.__pin = " "  # variables declared. it will be stored as __Atm__pin not __pn
        self.__balance = 0 # it will be stored as _Atm__balance not __balance
        self.__menu() # calling its own method
        print("hello")
        print(id(self)) # self is  each object address,sbi is self,hdfc is self . self belongs to the object with whom we are currently workin
        """
        in a class there are only data(variables in init) and methods that can only be accessed by its object no method can access another method not even init data
        the self in methods receives the object call(sbi.deposit()) as object as input in parenthesis like self inside method in class which matches
        when a method acesses  anather method it does by calling object(sbi as self) then method(self.deposit)        
        similarly when accessing data temp == self.pin
        so self is the current object , who called the method
        """
    def get_pin(self):
        return self.__pin
    def set_pin(self,new_pin):
        temp = input("enter your pin: ")
        if temp == self.__pin and type(new_pin) == str:
            self.__pin = new_pin
            print("pin changed")
        else:
            print("not allowed")



    def __menu(self):
        print("Hello how will you like to proceed?")
        while True:
            user_input = input( " enter 1 to create pin"
                               "enter 2 to deposit"
                               "enter3,4,5 to withdraw,to check balance,to exit ")

            if user_input == "1":
                print("create pin")
                self.create_pin()
            elif user_input == "3":
                print("withdraw")
                self.withdraw()
            elif user_input == "2":
                print("deposit")
                self.deposit()
            elif user_input == "4":
                print("checkbalance")
                self.check_balance()
            elif user_input == "5":
                print("exit")
                return False
            else:
                print("bye")
                return False

    def saved_pin(self):
        pass

    def create_pin(self):
        self.__pin = input("enter your pin: ")
        print("pin set successfully")

    def deposit(self):
        temp = input("enter your pin: ")
        if temp == self.__pin:
            amount = int(input("enter amt: "))
            self.__balance = self.__balance + amount
            print("deposit successful")
        else:
            print("invalid pin")

    def withdraw(self):
        temp = input("enter your pin: ")
        if temp == self.__pin:
            amount = int(input("enter amt: "))
            if amount < self.__balance:
                self.__balance = self.__balance - amount
                print("withdraw successful")
            else:
                print(" insufficient fund")

        else:
            print("invalid pin")

    def check_balance(self):
        temp = input("enter your pin: ")
        if temp == self.__pin:
            print(self.__balance)
        else:
            print("wrong pin")




sbi = Atm() # # sbi is the variable that stores the addreee of the object created Atm().this var is called reference var
#hdfc = Atm()
#print(id(sbi),"sbi")
#print(id(hdfc),"hdfc")

# sbi.(will show all methods and ins var like bal and pin).so if we write sbi.balance = "sfsf" we cannot add int to it
# so we have to hide data so that it cannot be changed. by puting __ in front of var or methods which we
# want to hide from customers we cnnot change its type or give input from outside of class

sbi.__balance = "dfgfdgfgd" # class does not recognize this var so it will be ignored
#sbi._Atm__balance = "dfgfd" this will change var type.maybe we __ classname
print(sbi.deposit())

print(sbi.check_balance())
sbi.set_pin(5.6)
sbi.get_pin()
sbi.set_pin("123456")
sbi.get_pin()




















