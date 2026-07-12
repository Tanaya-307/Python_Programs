import multiprocessing
import os

def Sum_even(No):
       sum = 0
       for i  in range(1,No+1):
              if (i % 2 == 0 ):
                   sum = sum + i
              
       print()
       print("process is running with pid :",os.getpid())
       print(f"Input number : {No}")
       print(f"sum of all even : {sum}")

       
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

    Result = pobj.map(Sum_even,Data)


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

process is running with pid : 17272
Input number : 1000000
sum of all even : 250000500000

process is running with pid : 7588
Input number : 2000000
sum of all even : 1000001000000

process is running with pid : 8
Input number : 3000000
sum of all even : 2250001500000

process is running with pid : 8024
Input number : 4000000
sum of all even : 4000002000000
'''