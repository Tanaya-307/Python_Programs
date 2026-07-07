def  Add(No1,No2):
    Addition = No1+No2
    return Addition

def main():
    print("Enter the 1st Number : ")
    no1 = int(input())

    print("Enter the 2nd Number : ")
    no2 = int(input())

    ret = Add(no1,no2)
    print("Addition is : ",ret)

    

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the 1st Number :
11
Enter the 2nd Number :
5
Addition is :  16
'''