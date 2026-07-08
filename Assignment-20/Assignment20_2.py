import threading

def Evenfactors(No):
    sum_even = 0
    print(f"Even factors of {No} are : ")

    for i in range(1,No+1):
        if (No % i==0 and i % 2 == 0):
            print (i,end=" ")
            sum_even = sum_even + i
    
    print()
    print(f"total sum : {sum_even}")

def Oddfactors(No):
    sum_odd = 0
    print(" ")
    print(f"Odd factors of {No} are : ")

    for i in range(1,No+1):
        if (No % i==0 and i % 2 != 0):
            print (i,end=" ")
            sum_odd = sum_odd + i

    print()
    print(f"total sum : {sum_odd}")


def main():
    print("Enter the Number : ")
    num =int(input())
    print(" ")

    t1=threading.Thread(target =Evenfactors,args=(num,))
    t1.start()
    t1.join()

    t2=threading.Thread(target =Oddfactors,args = (num,))
    t2.start()
    t2.join()

    print("Exit from main")

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the Number :
20

Even factors of 20 are :
2 4 10 20
total sum : 36

Odd factors of 20 are :
1 5
total sum : 6
Exit from main
'''