list_even = lambda lst : lst % 2==0

def main():
    lst = []

    print("Enter list")
    
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

    print("Data after filter : ",Fdata)

    
if __name__=="__main__":
    main() 