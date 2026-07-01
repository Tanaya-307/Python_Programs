def Divisible_3_and_5(No):

    if No%3 == 0 and  No%5==0:
        print(No,"is divisible by both 3 and 5")

    elif No%3==0:
        print(No,"is divisible by 3")

    else:
        print(No,"is divisible by only 5 ")


def main():

    print("Enter the number : ")

    Number = int(input())

    Divisible_3_and_5(Number)


if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the number :
15
15 is divisible by both 3 and 5
'''
