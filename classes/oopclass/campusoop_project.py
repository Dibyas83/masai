
# methods are special functions inside class , functions are outside class
# how to call them len() is a function.l.append() is a function inside of a listclass so it is a method so a listobject  only can use it

# variables are declared inside a special method called _init_ which has input called self



class Atm:
    def __init__(self):  # constructor is a method ,the codes inside it is automatically executed when we create a object of this class
        self.pin = " "  # variables declared
        self.balance = 0
        self.menu() # calling its own method
        print("hello")
        print(id(self)) # self is  each object address,sbi is self,hdfc is self . self belongs to the object with whom we are currently workin
        """
        in a class there are only data(variables in init) and methods that can only be accessed by its object no method can access another method not even init data
        the self in methods receives the object call(sbi.deposit()) as object as input in parenthesis like self inside method in class which matches
        when a method acesses  anather method it does by calling object(sbi as self) then method(self.deposit)        
        similarly when accessing data temp == self.pin
        so self is the current object , who called the method
        """
    def menu(self):
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


    def create_pin(self):
        self.pin = input("enter your pin: ")
        print("pin set successfully")

    def deposit(self):
        temp = input("enter your pin: ")
        if temp == self.pin:
            amount = int(input("enter amt: "))
            self.balance = self.balance + amount
            print("deposit successful")
        else:
            print("invalid pin")

    def withdraw(self):
        temp = input("enter your pin: ")
        if temp == self.pin:
            amount = int(input("enter amt: "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("withdraw successful")
            else:
                print(" insufficient fund")

        else:
            print("invalid pin")

    def check_balance(self):
        temp = input("enter your pin: ")
        if temp == self.pin:
            print(self.balance)
        else:
            print("wrong pin")




sbi = Atm() # every unger init will be auto executed " hello " will be printed
hdfc = Atm()
print(id(sbi),"sbi")
print(id(hdfc),"hdfc")


