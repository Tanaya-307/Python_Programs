from functools import reduce 

def prime(no):
    if no < 2:
        return False
    
    for i in range(2,int(no**0.5) + 1):
        if (no % i == 0 ):
            return False
    return True
            
Multiply = lambda no:no * 2
Maximum = lambda no1,no2:no1 if (no1>no2) else(no2)

def main():
    
    lst = []
    print("Enter the number of elements in List : ")
    No=int(input())

    print(f"Enter {No} elements in list : ")

    for i in range (0,No,1):
        lst.append(int(input()))

    print("input data is : ",lst)

    Fdata = list(filter(prime,lst))
    print("Data after filter : ",Fdata)

    Mdata = list(map(Multiply,Fdata))
    print("Data after map : ",Mdata)

    Rdata = reduce(Maximum,Mdata)
    print("Data after reduce is : ",Rdata)


if __name__=="__main__":
    main() 

'''
OUTPUT:
Enter the number of elements in List :
8
Enter 8 elements in list :
2
70
11
10
17
23
31
77
input data is :  [2, 70, 11, 10, 17, 23, 31, 77]
Data after filter :  [2, 11, 17, 23, 31]
Data after map :  [4, 22, 34, 46, 62]
Data after reduce is :  62
'''