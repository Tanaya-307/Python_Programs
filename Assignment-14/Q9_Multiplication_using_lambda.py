Multiplication = lambda no1,no2 :no1 * no2


def main():
    value1 = int(input("Enter 1st number : "))
    value2 = int(input("Enter 2nd number : "))

    ret = Multiplication(value1,value2)         

    print(f"Multiplication of {value1} and {value2} is {ret}")


if __name__=="__main__":
    main()  

'''
OUTPUT:
Enter number : 10
Enter number : 20
Multiplication of 10 and 20 is 200

'''