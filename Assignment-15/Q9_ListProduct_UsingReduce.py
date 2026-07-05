from functools import reduce

Product = lambda no1,no2: no1 * no2

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

    Rdata = reduce(Product,lst)

    print("Product of List is : ",Rdata)


if __name__=="__main__":
    main() 

'''
OUTPUT:
Enter list :
10
20
30
40
[10, 20, 30, 40]
Input data is :  [10, 20, 30, 40]
Product of List is :  240000
'''