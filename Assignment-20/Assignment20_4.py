import threading 

def small(name):
    count = 0
    for char in name :
        if char.islower():
            count = count + 1
    print("Thread name : ",threading.current_thread().name)
    print("Thread id for small letters: ",threading.get_ident())
    print(f"Thread id for lowercase letters: {count}")
    print()


def Capital(name):
    count = 0
    for char in name :
        if char.isupper():
            count = count + 1
    print("Thread name : ",threading.current_thread().name)
    print("Thread id for Capital letters : ",threading.get_ident())
    print(f"Upper case letters are: {count}")
    print()

def Digits(name):
    count = 0
    for char in name :
        if char.isdigit():
            count = count + 1
    print("Thread name : ",threading.current_thread().name)
    print("Thread id for Digits : ",threading.get_ident())
    print(f"Digits : {count}")
    print()


def main():

    user_input = input("Enter the string : ")
    print(" ")

    t1=threading.Thread(target =small,args=(user_input,))
    t1.start()
    t1.join()

    t2=threading.Thread(target =Capital,args = (user_input,))
    t2.start()
    t2.join()

    t3=threading.Thread(target =Digits,args = (user_input,))
    t3.start()
    t3.join()

    

    print("Exit from main")

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the string : MarveLLous37

Thread name :  Thread-1 (small)
Thread id for small letters:  9720
Thread id for lowercase letters: 8

Thread name :  Thread-2 (Capital)
Thread id for Capital letters :  7364
Upper case letters are: 3

Thread name :  Thread-3 (Digits)
Thread id for Digits :  8748
Digits : 2

Exit from main
'''