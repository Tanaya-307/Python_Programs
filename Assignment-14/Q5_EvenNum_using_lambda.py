checkeven = lambda no :(no % 2 == 0)


def main():
    value = int(input("enter number : "))

    ret = checkeven(value)          # ret = (value % 2 == 0)

    print(ret)

    if (ret==True):
        
        print("its even num")

    else : 
        print("its odd num")


if __name__=="__main__":
    main()  

'''
OUTPUT:
enter number : 10
True
its even num
'''