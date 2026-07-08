import threading

def Prime(data):

    print("\nPrime numbers are : ",end=" ")
    for no in data :
        is_prime = True
        for i in range(2,(no // 2) + 1):
            if no % i == 0:
                is_prime = False

        if is_prime:        
          print(no,end = " ")

def NonPrime(data):

    print("\nNon-prime numbers are : ",end=" ")
    for no in data :
        for i in range(2,(no // 2 )+ 1):
            if no % i == 0:
                print(no,end= " ")
                break

def main():

    print("Enter the number of elements :")
    n = int(input())

    elements=[]
    print(f"Enter {n} elements")
    

    for i in range (n):
        value = int(input())
        elements.append(value)
    print(f"list :{elements}")

    t1=threading.Thread(target =Prime,args=(elements,))
    t2=threading.Thread(target =NonPrime,args = (elements,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(" ")
    print("Exit from main")

if __name__=="__main__":
    main()