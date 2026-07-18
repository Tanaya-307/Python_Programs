class Arithmetic:
    
    def __init__(self):
        self.value_1 = 0
        self.value_2 = 0

    def Accept(self):
        self.value_1 = int(input("Enter the 1st Number : "))
        self.value_2 = int(input("Enter the 2nd Number : "))

    def add(self):
        return self.value_1 + self.value_2
    
    def sub(self):
        return self.value_1 - self.value_2
    
    def mul(self):
        return self.value_1 * self.value_2
    
    def div(self):
        if self.value_2 ==0:
            print("Division by zero is not allowed ")
        return self.value_1 / self.value_2

print("---Object 1---")
obj1 = Arithmetic()
obj1.Accept()
print("Addition :",obj1.add())
print("Subtraction :",obj1.sub())
print("Multiplication :",obj1.mul())
print("Division :",obj1.div())

print()
print("---Object 2---")
obj2 = Arithmetic()
obj2.Accept()
print("Addition :",obj2.add())
print("Subtraction :",obj2.sub())
print("Multiplication :",obj2.mul())
print("Division :",obj2.div())

'''
OUTPUT:
---Object 1---
Enter the 1st Number : 11
Enter the 2nd Number : 21
Addition : 32
Subtraction : -10
Multiplication : 231
Division : 0.5238095238095238

---Object 2---
Enter the 1st Number : 51
Enter the 2nd Number : 0
Addition : 51
Subtraction : 51
Multiplication : 0
Division by zero is not allowed
'''

