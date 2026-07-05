from functools import reduce


Addition = lambda no1,no2:no1+no2

def main():
    lst = []

    print("Enter list : ")
    
    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)

    print(lst)

    print("Input data is : ",lst)

    Rdata = reduce(Addition,lst)

    print("data after reduce is : ",Rdata)


if __name__=="__main__":
    main() 

'''
OUTPUT:
Enter list :
10
20
30
5
1
2
[10, 20, 30, 5, 1, 2]
Input data is :  [10, 20, 30, 5, 1, 2]
data after reduce is :  68
'''