checkdivisible = lambda no :(no % 5 == 0)


def main():
    value = int(input("enter number : "))

    ret = checkdivisible(value)          # ret = (value % 2 == 0)

    print(ret)

    if (ret==True):
        
        print(f"{value} is divisible by 5")

    else : 
        print(f"{value} is not divisbile by 5")


if __name__=="__main__":
    main()  

'''
OUTPUT:
1- enter number : 10
   True
   10 is divisible by 5

2 -enter number : 9
   False
   9 is not divisbile by 5

'''