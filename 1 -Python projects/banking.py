from sympy.core.random import choice


class Acc: # console flow
    balance = 23.23456

    def show_balance(self):
        print(f"you balance is ${self.balance: .2f}")

    def deposit(self):
        amt = float(input("Enter amt to be deposited"))
        if amt < 0:
            print("not valid")
            return 0
        else:
            return amt

    def withdraw(self):
        amt = float(input("Enter amt to be withdrawn: "))

        if amt > self.balance:
            print("insufficient balance")
            return 0
        elif amt < 0:
            print("amt should be greater than 0")
            return 0
        else:
            return amt


    def create_acc(user_file):# accounts.txt
        pass
        """
        in dict,json and txt file
        acc_no,name,password,balance = data
        enter your name,initial deposit,acc no,password
        acc created sucess
        others should not have this
        """
    def login(self,username,password):
        pass
        """
        Enter your acc_no
        enter your password-******  (hashing or encryption can be done)
        login sucessful welcome mr ---

        acc file - write during creation,read acc detail during validation
        """

    def process(self):

        is_running = True
        while is_running:
            print(" HDFC Banking System - Please Select")
            print("1-Show Balance")
            print("2- Deposit")
            print("3-Withdraw")
            print("4-Exit")
            make_choice = input("Enter your choice 1 to 4: ")

            if make_choice == "1":
                self.show_balance()
            elif make_choice == "2":
                self.balance += self.deposit()
            elif make_choice == "3":
                self.balance -= self.withdraw()
            elif make_choice == "4":
                is_running = False
            else:
                print("that is not valid choice")
        print("have a nice day")

    def exit(showbal,trans_done):
        pass

    #enter your choice
    def transaction_prcess(login,transactionrecord_filehandling):
        pass


    """
    transactions.txt,depo,withrawl,date,include error handling,invalid input,insufficient balance or incorrect credentials
        bank statement
        interest

    transaction_file = accno,transaction type,amt,date
    """
    def finance_mangement(storaje , insurance, loans):
        pass

    #privilege levels

hd = Acc()
hd.process()
# use main






















