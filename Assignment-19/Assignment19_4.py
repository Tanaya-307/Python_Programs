from functools import reduce 

checkeven = lambda no:(no % 2 == 0)
square = lambda no:no ** 2
Addition = lambda no1,no2:no1+no2

def main():
    
    lst = []
    print("Enter the number of elements in List : ")
    No=int(input())

    
    print(f"Enter {No} elements in list : ")

    for i in range (0,No,1):
        lst.append(int(input()))
    

    print("input data is : ",lst)

    Fdata = list(filter(checkeven,lst))
    print("Data after filter : ",Fdata)

    Mdata = list(map(square,Fdata))
    print("Data after map : ",Mdata)

    Rdata = reduce(Addition,Mdata)
    print("Data after reduce is : ",Rdata)

if __name__=="__main__":
    main() 

'''
OUTPUT:
Enter the number of elements in List :
10
Enter 10 elements in list :
5
2
3
4
3
4
1
2
8
10
input data is :  [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
Data after filter :  [2, 4, 4, 2, 8, 10]
data after map :  [4, 16, 16, 4, 64, 100]
data after reduce is :  204
'''