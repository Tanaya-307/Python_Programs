def max_value(data):
    max_num = data[0]

    for no in data:
        if no > max_num:
            max_num = no
    return max_num

def main():
    print("Enter the number of elements :")
    n = int(input())

    elements=[]
    print(f"Enter {n} elements :")
    for i in range (n):
        value = int(input())
        elements.append(value)
    print(f"list is :{elements}")

    result = max_value(elements)
    print(f"Maximum element is : {result}")

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the number of elements :
7
Enter 7 elements :
13
5
45
7
4
56
34
list is :[13, 5, 45, 7, 4, 56, 34]
Maximum element is : 56

'''