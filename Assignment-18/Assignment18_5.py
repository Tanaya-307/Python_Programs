import MarvellousNum  

def sumPrime(No):
    Total_sum = 0

    for n in No:
        if (MarvellousNum.ChkPrime(n)):
            Total_sum = Total_sum + n
    return Total_sum

def main():
    print("Enter the number of elements :")
    n = int(input())

    elements=[]
    print(f"Enter {n} elements :")

    for i in range (n):
        value = int(input())
        elements.append(value)
    print(f"list is :{elements}")

    result = sumPrime(elements)
    print(f"Sum of all prime Numbers is : {result}")

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the number of elements :
11
Enter 11 elements :
13
5
45
7
4
56
10
34
2
5
8
list is :[13, 5, 45, 7, 4, 56, 10, 34, 2, 5, 8]
Sum of all prime Numbers is : 32

'''