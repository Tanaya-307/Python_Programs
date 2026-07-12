import multiprocessing
import os
import time

def power_5(No):
       pow = 1
       for i  in range(1,No+1):
             pow = i ** 5
       return pow
       
def main():
    print("Enter the number of elements :")
    n = int(input())

    Data=[]
    print(f"Enter {n} elements")
    

    for i in range (n):
        value = int(input())
        Data.append(value)
    print(f"list :{Data}")
       
    Result = []

    start_time = time.perf_counter()

    pobj=multiprocessing.Pool()

    Result = pobj.map(power_5,Data)

    pobj.close()
    pobj.join()


    end_time = time.perf_counter()

    print("Result is ")
    print(Result)
    print(f"time required : {end_time-start_time:.4f}seconds")
       

if __name__=="__main__":
       main()

'''
OUTPUT:
Enter the number of elements :
4
Enter 4 elements
1
2
3
4
list :[1, 2, 3, 4]
Result is
[1, 32, 243, 1024]
time required : 0.5090seconds

'''
