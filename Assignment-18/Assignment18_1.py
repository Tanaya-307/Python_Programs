def ElementSum(data):
    sum = 0
    for no in data:
        sum =sum+no
    return sum

def main():
    print("Enter the number of elements :")
    n = int(input())

    elements=[]
    print(f"Enter {n} elements :")
    for i in range (n):
        value = int(input())
        elements.append(value)
    print(f"lis is :{elements}")

    result = ElementSum(elements)
    print(f"Addition is : {result}")

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the number of elements :
6
Enter 6 elements :
13
5
45
7
4
56
lis is :[13, 5, 45, 7, 4, 56]
Addition is : 130

'''