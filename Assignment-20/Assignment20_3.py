import threading

def EvenList(data):
    print("\nEven numbers are : ",end=" ")
    for No in (data):
        if (No % 2==0 ):
            print (No,end=" ")
    print() 

def OddList(data):
    print("\nOdd Numbers are : ",end=" ")

    for No in (data):
        if (No % 2!=0):
            print (No,end=" ")
    print()


def main():

    print("Enter the number of elements :")
    n = int(input())

    elements=[]
    print(f"Enter {n} elements")
    

    for i in range (n):
        value = int(input())
        elements.append(value)
    print(f"list :{elements}")

    t1=threading.Thread(target =EvenList,args=(elements,))
    t2=threading.Thread(target =OddList,args = (elements,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(" ")
    print("Exit from main")

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the number of elements :
7
Enter 7 elements
13
11
7
4
36
34
80
list :[13, 11, 7, 4, 36, 34, 80]

Even numbers are :  4 36 34 80

Odd Numbers are :  13 11 7

Exit from main
'''
