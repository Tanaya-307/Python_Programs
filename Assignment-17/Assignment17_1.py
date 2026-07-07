import Arithmetic

def main():
    print("Enter the 1st num :")
    value1 = int(input())

    print("Enter the 2nd num :")
    value2 = int(input())

    Addition = Arithmetic.Add(value1,value2)
    print("Addition is : ",Addition)

    Subtraction = Arithmetic.Sub(value1,value2)
    print("Subtraction is : ",Subtraction)

    Multiplication = Arithmetic.Mult(value1,value2)
    print("Multiplication is : ",Multiplication)

    Division = Arithmetic.Div(value1,value2)
    print("Division is : ",Division)

if __name__=="__main__":
    main() 

'''
OUTPUT:
Enter the 1st num :
20
Enter the 2nd num :
10
Addition is :  30
Subtraction is :  10
Multiplication is :  200
Division is :  2.0

'''



