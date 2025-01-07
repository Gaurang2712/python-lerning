# Design a BankAccount class with attributes for account number, holder name, and balance. Include methods for deposit, withdrawal, and displaying account information.


class BankAccount:
    account=""
    acnumber=0
    name=""
    balance=0

    def addvalues(self,a,an,n,b):
        self.account=a
        self.acnumber=an
        self.name=n
        self.balance=b
    
    def deposit(self,depo):
        self.balance=self.balance+depo
    
    def withdrawal(self,wid):
        self.balance=self.balance-wid
    
    def display(self):
        print(self.account,self.acnumber,self.name,self.balance)


customer1=BankAccount()

customer1.addvalues(input("Enter type account:-"),int(input("Enter account number:-")),input("Enter Customer name:-"),int(input("Enter account balance:-")))
customer1.display()

customer1.deposit(int(input("Enter value to deposit:-")))

customer1.display()

customer1.withdrawal(int(input("Enter value to Withdrawal:-")))

customer1.display()