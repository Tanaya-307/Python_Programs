class Numbers:

    def __init__(self):
        self.Value = int(input("Enter a number: "))

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2, int(self.Value**0.5) + 1):
            if self.Value % i == 0:
                return False
        return True

    def ChkPerfect(self):
        if self.Value <= 1:
            return False
        
        sum_divisors = 0
        for i in range(1, self.Value):
            if self.Value % i == 0:
                sum_divisors += i
                
        return sum_divisors == self.Value

    def Factors(self):
        print(f"Factors of {self.Value}: ", end="")
        factors_list = []
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                factors_list.append(str(i))
        print(", ".join(factors_list))

    def SumFactors(self):
        sum_all = 0
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                sum_all += i
        return sum_all



print("--- Object 1 ---")
num1 = Numbers()
print(f"Is Prime: {num1.ChkPrime()}")
print(f"Is Perfect: {num1.ChkPerfect()}")
num1.Factors()
print(f"Sum of all factors: {num1.SumFactors()}")

print("\n--- Object 2 ---")
num2 = Numbers()
print(f"Is Prime: {num2.ChkPrime()}")
print(f"Is Perfect: {num2.ChkPerfect()}")
num2.Factors()
print(f"Sum of all factors: {num2.SumFactors()}")

'''
OUTPUT:
--- Object 1 ---
Enter a number: 10
Is Prime: False
Is Perfect: False
Factors of 10: 1, 2, 5, 10
Sum of all factors: 18

--- Object 2 ---
Enter a number: -10
Is Prime: False
Is Perfect: False
Factors of -10:
Sum of all factors: 0
'''