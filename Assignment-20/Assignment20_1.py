import threading

def Even():
    count = 2
    Num = 0

    while Num <= 9:

        if (count % 2==0):

            print(count,end=" ")
            Num = Num + 1
        count = count + 1

def Odd():
    count = 1
    Num = 0

    while Num <= 9:

        if (count % 2!=0):

            print(count,end=" ")
            Num = Num + 1
        count = count + 1

def main():

    t1=threading.Thread(target=Even)
    t2=threading.Thread(target=Odd)
    print("\nFirst 10 even Numbers are : ",end=" ")
    t1.start()
    t1.join()
    print(" ")

    print("\nFirst 10 Odd Numbers are : ",end=" ")
    t2.start()
    t2.join()

if __name__=="__main__":
    main()

'''
OUTPUT:
First 10 even Numbers are :  2 4 6 8 10 12 14 16 18 20

First 10 Odd Numbers are :  1 3 5 7 9 11 13 15 17 19
'''


    