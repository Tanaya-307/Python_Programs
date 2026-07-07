from functools import reduce

NumInRange = lambda no:no>=70 and no<=90
Increament = lambda no:no + 10
Product = lambda no1,no2:no1 *no2

def main():
    
    lst = []
    print("Enter the number of elements in List : ")
    No=int(input())

    
    print(f"Enter {No} elements in list : ")

    for i in range (0,No,1):
        lst.append(int(input()))
    

    print("input data is : ",lst)

    Fdata = list(filter(NumInRange,lst))
    print("Data after filter : ",Fdata)

    Mdata = list(map(Increament,Fdata))
    print("data after map : ",Mdata)

    Rdata = reduce(Product,Mdata)
    print("data after reduce is : ",Rdata)


if __name__=="__main__":
    main() 

'''
OUTPUT:
Enter the number of elements in List :
12
Enter 12 elements in list :
4
34
36
76
68
24
89
23
86
90
45
70
input data is :  [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
Data after filter :  [76, 89, 86, 90, 70]
data after map :  [86, 99, 96, 100, 80]
data after reduce is :  6538752000
'''
 