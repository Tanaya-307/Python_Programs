from functools import reduce

Maximum = lambda no1,no2:no1 if(no1>no2) else (no2)

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

    Rdata = reduce(Maximum,lst)

    print("Max number is : ",Rdata)


if __name__=="__main__":
    main() 

'''
OUTPUT:
Enter list :
1
2
4
8
[1, 2, 4, 8]
Input data is :  [1, 2, 4, 8]
Max number is :  8
'''
