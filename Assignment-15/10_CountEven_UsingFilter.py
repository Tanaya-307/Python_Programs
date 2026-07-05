list_even = lambda no:no if(no % 2==0)else()

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

    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)

    print(lst)

    print("Input data is : ",lst)
    Fdata = list(filter(list_even,lst))
    print("Even numbers  : ",Fdata)

    Fdata = len(list(filter(list_even,lst)))
    print("count of even numbers after filter : ",Fdata)

    
if __name__=="__main__":
    main()  

'''
OUTPUT:
2
4
10
73
51
20
[2, 4, 10, 73, 51, 20]
Input data is :  [2, 4, 10, 73, 51, 20]
Even numbers  :  [2, 4, 10, 20]
count of even numbers after filter :  4
'''