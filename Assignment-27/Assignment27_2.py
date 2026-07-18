class BankAccount:

    ROI = 10.5

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def display(self):
        print("name : ",self.name)
        print("amount : ",self.amount)

    def deposit(self,amount):
        if amount>0:
            self.amount +=amount
            print("Deposited amount: ",amount)
            print("New Balance : ",self.amount)
        else:
            print("Invalid input")

    def withdraw(self,amount):
        if amount > self.amount :
            print("Insufficient Balance")
        elif amount<= 0:
            print("Invalid input")
        else:
            self.amount -= amount
            print("Withdraw amount: ",amount)
            print("New Balance : ",self.amount)

    def calculateInterest(self):
        interest = (self.amount*BankAccount.ROI)/100
        return interest
    
acc1 = BankAccount("Tina",5000)
acc1.display()
acc1.deposit(15000)
acc1.withdraw(2000)
print("Interest : ",acc1.calculateInterest())

print()
print("---account 2---")
acc2 = BankAccount("Rita",10000)
acc2.display()
acc2.withdraw(2000)
print("Interest : ",acc2.calculateInterest())

'''
OUTPUT:
name :  Tina
amount :  5000
Deposited amount:  15000
New Balance :  20000
Withdraw amount:  2000
New Balance :  18000
Interest :  1890.0

---account 2---
name :  Rita
amount :  10000
Withdraw amount:  2000
New Balance :  8000
Interest :  840.0

'''



