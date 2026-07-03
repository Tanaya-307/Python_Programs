def prime(Num):
    for i in range(2,Num):
        if (Num % i == 0 ):
            print(Num,"is not prime Number")
            break
        else :
            print(Num,"is prime Number ")
            break


def main():
    print("Enter the Number : ")
    No = int(input())
    prime(No)

if __name__=="__main__":
    main()

'''
Enter the Number :
11
11 : is prime Number

'''

   