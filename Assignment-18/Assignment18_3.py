def min_value(data):
    min_num = data[0]

    for no in data:
        if no < min_num:
            min_num = no
    return min_num

def main():
    print("Enter the number of elements :")
    n = int(input())

    elements=[]
    print(f"Enter {n} elements")
    

    for i in range (n):
        value = int(input())
        elements.append(value)
    print(f"list :{elements}")
        

    result = min_value(elements)
    print(f"Minimum element is : {result}")

if __name__=="__main__":
    main()

'''
OUTPUT:

Enter the number of elements :
4
Enter 4 elements
13
5
45
7
list :[13, 5, 45, 7]
Minimum element is : 5

'''