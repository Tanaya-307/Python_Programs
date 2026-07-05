checkodd = lambda no :(no % 2 != 0)


def main():
    value = int(input("Enter number : "))

    ret = checkodd(value)          # ret = (value % 2 == 0)

    print(ret)

    if (ret==True):
        
        print("its odd num")

    else : 
        print("its even num")


if __name__=="__main__":
    main()  

'''
OUTPUT:
Enter number : 10
False
its even num
'''