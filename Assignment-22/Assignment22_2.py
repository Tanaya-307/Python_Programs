import multiprocessing
import os


def factorial(No):
       fact = 1
       print("process is running with pid :",os.getpid())

       for i  in range(1,No+1):
              fact = fact * i
       return fact
       
def main():
    print("Enter the number of elements :")
    n = int(input())

    Data=[]
    print(f"Enter {n} elements")

    Result = []

    for i in range (n):
        value = int(input())
        Data.append(value)
    print(f"input :{Data}")
    

    pobj=multiprocessing.Pool()

    Result = pobj.map(factorial,Data)

    pobj.close()
    pobj.join()
    
    print("Result is ")
    print(Result)
    

if __name__=="__main__":
       main()

'''
OUTPUT:
Enter the number of elements :
4
Enter 4 elements
10
15
20
25
input :[10, 15, 20, 25]
process is running with pid : 6128

Result is
[3628800, 1307674368000, 2432902008176640000, 15511210043330985984000000]

'''