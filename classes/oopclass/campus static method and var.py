


class Atm:
    __counter = 1

    def __init__(self):
        self.__pin = " "
        self.__balance = 0
        #self.Sno = 0
        #self.Sno += 1 # will not work for instance var,as it becomes 0 everytime for each objects and does not accumulate
        self.Sno = Atm.__counter # class var is called through class
        Atm.__counter += 1

        #self.__menu()
        print(self.Sno)
        """
        instance var is different for diff objects
        static or class var is same for all objects
        """

    @staticmethod
    def get_countr(): # self not used in static method
        return Atm.__counter

    @staticmethod
    def set_countr(new):
        #temp = input("enter your pin: ")
        #if temp == self.__pin and type(new) == int:  self does not work here
        if type(new) == int:
            Atm.__counter = new
            print("countr changed")
        else:
            print("not allowed")

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




c1 = Atm()
c2 = Atm()
c3 = Atm()
print(c2.Sno)
"""
1
2
3
2
"""
print(c3.Sno)
print(c3.get_countr(),"getc3") # when c3 is object sno is 3 but counter inc to 4
c3.set_countr(8)
print(c3.get_countr())


















