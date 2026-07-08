def Frequency(data,value):
    count = 0

    for no in data:
        if no == value:
            count = count+1
    return count

def main():
    print("Enter the number of elements :")
    n = int(input())

    elements=[]
    print(f"Enter {n} elements")
    

    for i in range (n):
        value = int(input())
        elements.append(value)
    print(f"list :{elements}")

    print("Element to search :")
    search =int(input())


    result = Frequency(elements,search)
    print(f"Frequency of {search} in List is : {result}")

if __name__=="__main__":
    main()

'''
OUTPUT:

Enter the number of elements :
11
Enter 11 elements
13
5
45
7
4
56
5
34
2
5
65
list :[13, 5, 45, 7, 4, 56, 5, 34, 2, 5, 65]
Element to search :
5
Frequency of 5 in List is : 3

'''