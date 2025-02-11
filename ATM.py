'''
 Atm Machine - create a program that simulate the all operations (Account Balance, Cash Withdraw, Cash Deposit,
    Pin Change, transaction)
'''


class ATM:

    def __init__(self, Account_Number=123456789, PIN=2345,  Balance=100):
        self.Account_number = Account_Number
        self.Pin = PIN
        self.Balance = Balance
        self.Transaction_history = []

# Bank account login
    def login(self):
        Account_Number = int(input("Enter your Account number:"))
        PIN = int(input("Enter your Account Password/PIN:"))
        if Account_Number == self.Account_number and PIN == self.Pin :
            print("Login Successfully.")

        elif Account_Number != self.Account_number and PIN != self.Pin or Account_Number == self.Account_number and\
                PIN != self.Pin or Account_Number != self.Account_number and PIN == self.Pin:
            print(" Opps, try again...")
            return self.login()

# check balance
    def Account_balance(self):
        print(f"your balance is : {self.Balance} ")

# cash withdraw
    def Cash_Withdraw(self, Amount):

        if Amount <= self.Balance and Amount > 0:
            self.Balance -= Amount
            self.Transaction_history.append(f"Withdrawal of {Amount}")
            print(f"{Amount} Withdraw successfully.")
        elif Amount > self.Balance:
            print("insufficient amount , please check amount and try again.")
        else:
            print("Invalid Withdrawal Amount.")

# cash deposit
    def Cash_Deposite(self, Amount):

        if Amount > 0:
            self.Balance += Amount
            self.Transaction_history.append(f"Deposit of {Amount}")
            print(f"{Amount} Deposit successfully.")
        else:
            print("Amount is not valid,please try again.")

# change PIN
    def PIN_Change(self, New_PIN):
        self.Pin = New_PIN
        print("PIN change successfully.")

# transaction history
    def Transaction_History(self):
        print(f"transaction history:{self.Transaction_history}.")

# Driver code
c1 = ATM()
choice1 = 0
while choice1 != 3:
    print("\n****************WELCOME TO ATM MACHINE*********************")
    print("\n1.Login your Bank Account")
    print("\n2.exit")
    choice1 = int(input("Enter your choice:"))
    if choice1 == 1:
        c1.login()

        choice2 = 0
        while choice1 != 7:
            print("\n************ATM MACHINE OPERATIONS***************")
            print("\n1.Account Balance")
            print("\n2.Cash Withdraw")
            print("\n3.Cash Deposit")
            print("\n4.Pin Change")
            print("\n5.Transaction History")
            print("\n6.Exit")
            choice2 = int(input("Enter your choice:"))

            if choice2 == 1:
                c1.Account_balance()

            elif choice2 == 2:
                Amount = float(input("Enter amount to be withdraw:"))
                c1.Cash_Withdraw(Amount)

            elif choice2 == 3:
                Amount = float(input("Enter an amount to be deposit:"))
                c1.Cash_Deposite(Amount)

            elif choice2 == 4:
                New_PIN = str(input("Enter your new Password/PIN:"))
                c1.PIN_Change(New_PIN)

            elif choice2 == 5:
                c1.Transaction_History()

            elif choice2 == 6:
                print("All Operations Done Successfully")
                break

            else:
                print("Invalid choice.")

    elif choice1 == 2:
        print("THANK YOU!!!")
        break