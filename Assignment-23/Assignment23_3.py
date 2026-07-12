import multiprocessing
import os

def Even_count(No):
       
       count = 0
       for i  in range(1,No+1):
              if (i % 2 == 0 ):
                   count = count + 1
              
       print()
       print("process is running with pid :",os.getpid())
       print(f"Input number : {No}")
       print(f"Even count is : {count}")

       
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

    Result = pobj.map(Even_count,Data)


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

process is running with pid : 7088
Input number : 1000000
Even count is : 500000

process is running with pid : 16836
Input number : 2000000
Even count is : 1000000

process is running with pid : 9464
Input number : 3000000
Even count is : 1500000

process is running with pid : 5928
Input number : 4000000
Even count is : 2000000
'''
