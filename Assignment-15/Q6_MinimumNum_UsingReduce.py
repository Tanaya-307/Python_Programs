from functools import reduce

Minimum = lambda no1,no2:no1 if(no1<no2) else (no2)

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

    print(lst)

    print("Input data is : ",lst)

    Rdata = reduce(Minimum,lst)

    print("Minimum number is : ",Rdata)


if __name__=="__main__":
    main() 

'''
OUTPUT:
Enter list :
10
32
11
21
[10, 32, 11, 21]
Input data is :  [10, 32, 11, 21]
Minimum number is :  10
'''