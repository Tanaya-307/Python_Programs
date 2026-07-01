def chkGreater(No1,No2):
    if No1>No2:
        print(No1,"is Greater")
    elif No2>No1:
        print(No2,"is Greater")
    else:
        print("Both",No1,No2,"are equal")

def main():
    print("Enter the 1st  Number : ")
    Num1 = int(input())
    print(" ")

    print("Enter the 2nd Number : ")
    Num2 = int(input())
    print(" ")

    chkGreater(Num1,Num2)

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the 1st  Number :
10

Enter the 2nd Number :
20

20 is Greater

'''

