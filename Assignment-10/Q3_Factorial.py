def print_Factorial(Num):
    Factorial = 1
    for i in range(1,Num+1):
        Factorial = Factorial * i
    
    print("Factorial of ",Num,"is :",Factorial)

def main():
    print("Enter the Number : ")
    no = int(input())
    print_Factorial(no)

if __name__=="__main__":
    main()