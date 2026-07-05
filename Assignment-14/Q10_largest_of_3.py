checkmax = lambda no1,no2,no3 :no1 if(no1>=no2 and no1>=no2)else(no2 if no2>=no3 else no3)

def main():
    value1 = int(input("Enter 1st number : "))
    value2 = int(input("Enter 2nd number : "))
    value3 = int(input("Enter 3rd number : "))

    ret = checkmax(value1,value2,value3)          

    print(f"{ret} is max")


if __name__=="__main__":
    main()  

'''
OUTPUT:
Enter 1st number : 10
Enter 2nd number : 20
Enter 2nd number : 30
30is max
'''