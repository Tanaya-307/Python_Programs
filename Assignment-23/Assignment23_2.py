import multiprocessing
import os

def Sum_odd(No):
       sum = 0
       for i  in range(1,No+1):
              if (i % 2 != 0 ):
                   sum = sum + i
              
       print()
       print("process is running with pid :",os.getpid())
       print(f"Input number : {No}")
       print(f"sum of all Odd numbers  : {sum}")

       
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

    Result = pobj.map(Sum_odd,Data)

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

process is running with pid : 6448
Input number : 1000000
sum of all Odd numbers  : 250000000000

process is running with pid : 18044
Input number : 2000000
sum of all Odd numbers  : 1000000000000

process is running with pid : 18580
Input number : 3000000
sum of all Odd numbers  : 2250000000000

process is running with pid : 14288
Input number : 4000000
sum of all Odd numbers  : 4000000000000
'''