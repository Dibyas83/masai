
class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def calculate_interest(self):
        pass

class SavingsAccount(BankAccount):
    def __init__(self,account_number,balance,interest_rate):
        super().__init__(account_number,balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return (self.balance * self.interest_rate)/100


class FixedDepositAccount(BankAccount):
    def __init__(self,account_number,balance,interest_rate,duration_year):
        super().__init__(account_number,balance,)
        self.interest_rate = interest_rate
        self.duration_year = duration_year

    def calculate_interest(self):
        return (self.balance * self.interest_rate*self.duration_year)/100



N = int(input())
accounts = []
for _ in range(N):
    data = input().split(" ")
    acc_typ = data[0]
    acc_no = data[1]
    balanc = float(data[2])
    int_rata = float(data[3])
    years = int(data[4])

    if acc_typ == "SavingsAccount":
        accounts.append(SavingsAccount(acc_no,balanc,int_rata))
    elif acc_typ == "FixedDepositAccount":
        accounts.append(FixedDepositAccount(acc_no,balanc,int_rata,years))
print(accounts)


for account in accounts:
    interest = account.calculate_interest()
    print(f"{account.account_number} {interest:.2f}")







































