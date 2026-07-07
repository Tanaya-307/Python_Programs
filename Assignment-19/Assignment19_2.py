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
1.Enter 1st number : 4
  Enter 2nd number : 3
  Multiplication of 4 and 3 is 12

2.Enter 1st number : 6
  Enter 2nd number : 3
  Multiplication of 6 and 3 is 18
'''