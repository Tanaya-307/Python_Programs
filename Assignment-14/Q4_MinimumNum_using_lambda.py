checkmin = lambda no1,no2 :(no1>no2)

def main():
    value1 = int(input("enter 1st number : "))
    value2 = int(input("enter 2nd number : "))

    ret = checkmin(value1,value2)          # ret = (value % 2 == 0)

    print(ret)

    if (value1 > value2): 

        print(f"{value2} is min ")

    else : 
        print(f"{value1} is min")


if __name__=="__main__":
    main()  

'''
OUTPUT:
enter 1st number : 10
enter 2nd number : 20
False
10 is min
'''