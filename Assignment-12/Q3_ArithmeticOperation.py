def Addition(Num1,Num2):
    Add = Num1 + Num2
    return ("Addition",Add)

def Subtraction(Num1,Num2):
     Sub = Num1 - Num2
     return ("Subtraction",Sub)

def Multiplication(Num1,Num2):
     mult = Num1 * Num2
     return ("Multiplication",mult)

def Division(Num1,Num2):
     Div = Num1 / Num2
     return ("Division",Div)

def main():
    print("Enter the 1st Number : ")
    No1 = int(input())
    print("Enter the 2nd Number")
    No2 = int(input())

    print(Addition(No1,No2))
    print(Subtraction(No1,No2))
    print(Multiplication(No1,No2))
    print(Division(No1,No2))


if __name__=="__main__":
    main()