checkmax = lambda no1,no2 :(no1>no2)

def main():
    value1 = int(input("enter 1st number : "))
    value2 = int(input("enter 2nd number : "))

    ret = checkmax(value1,value2)          

    print(ret)

    if (value1 > value2): 

        print(f"{value1} is max")

    else : 
        print(f"{value2} is max")


if __name__=="__main__":
    main()  

'''
OUTPUT : 
enter 1st number : 10
enter 2nd number : 20
False
20 is max
'''