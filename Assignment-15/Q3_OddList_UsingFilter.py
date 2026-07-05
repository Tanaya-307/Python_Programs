list_odd = lambda lst : lst % 2!=0

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

    Fdata = list(filter(list_odd,lst))

    print("Data after filter : ",Fdata)

    
if __name__=="__main__":
    main() 


'''
OUTPUT:
Enter list :
11
21
51
101
50
10
[11, 21, 51, 101, 50, 10]
Input data is :  [11, 21, 51, 101, 50, 10]
Data after filter :  [11, 21, 51, 101]
'''