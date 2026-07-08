import threading

def Maximum(data):
    max_val = data[0]
    for no in data:
        if no > max_val:
            max_val = no

    print("Maximum  number from list is :",max_val)

def Minimum(data):
    min_val = data[0]
    for no in data:
        if no < min_val:
            min_val = no

    print("Minimum number from list  is :",min_val)



def main():

    print("Enter the number of elements :")
    n = int(input())

    elements=[]
    print(f"Enter {n} elements")
    

    for i in range (n):
        value = int(input())
        elements.append(value)
    print(f"list :{elements}")

    t1=threading.Thread(target =Maximum,args=(elements,))
    t2=threading.Thread(target =Minimum,args = (elements,))

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
11
Enter 11 elements
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
list :[13, 5, 45, 7, 4, 56, 10, 34, 2, 5, 8]
Maximum  number from list is : 56
Minimum number from list  is : 2

Exit from main


'''