import multiprocessing
import os

def factorial(No):
       fact = 1
    
       for i  in range(1,No+1):
              fact = fact * i
                   
       print()
       print("process is running with pid :",os.getpid())
       print(f"Input number : {No}")
       print(f"factorial of {No} is : {fact}")

       
def main():
    print("Enter the number of elements :")
    n = int(input())

    Data=[]
    print(f"Enter {n} elements")
    

    for i in range (n):
        value = int(input())
        Data.append(value)
    print(f"list :{Data}")

    
    pobj=multiprocessing.Pool()

    Result = pobj.map(factorial,Data)


    pobj.close()
    pobj.join()

      
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
list :[10, 15, 20, 25]

process is running with pid : 984
Input number : 10
factorial of 10 is : 3628800


process is running with pid : 984
process is running with pid : 13448
Input number : 15
Input number : 20
factorial of 15 is : 1307674368000
factorial of 20 is : 2432902008176640000

process is running with pid : 984
Input number : 25
factorial of 25 is : 15511210043330985984000000
'''