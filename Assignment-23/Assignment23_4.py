import multiprocessing
import os

def Odd_count(No):
       
       count = 0
       for i  in range(1,No+1):
              if (i % 2 != 0 ):
                   count = count + 1
              
       print()
       print("process is running with pid :",os.getpid())
       print(f"Input number : {No}")
       print(f"count is : {count}")

       
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

    Result = pobj.map(Odd_count,Data)
    print(f"result is : {Result.count}")


    pobj.close()
    pobj.join()
    

      
if __name__=="__main__":
       main()

'''
OUTPUT:
Enter the number of elements :
4
Enter 4 elements
1000000
2000000
3000000
4000000
list :[1000000, 2000000, 3000000, 4000000]

process is running with pid : 5872
Input number : 1000000
count is : 500000

process is running with pid : 2924
Input number : 2000000
count is : 1000000

process is running with pid : 10700
Input number : 3000000
count is : 1500000

process is running with pid : 13684
Input number : 4000000
count is : 2000000

'''