def Factorial(No):
    ret = 1
    for i in range(1,No+1):
        ret = ret * i
    return ret

def main():
    value = int(input("Enter the input :"))
    Res = Factorial(value)
    print(f"Factorial of {value} is {Res}")

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the input :5
Factorial of 5 is 120
'''