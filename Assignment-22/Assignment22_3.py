import multiprocessing

def prime(No):
       count = 0
       if No < 2:return False

       for i  in range(2, int(No ** 0.5) + 1):
             if No % i == 0:
                   return False
             else: 
                   count = count+1
                   return True
            
       
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

    Result = pobj.map(prime,Data)
    
    
    pobj.close()
    pobj.join()
    
    print(f"count of prime is :{Result.count(True)}")
    print("Result is ")
    print(Result)
    

if __name__=="__main__":
       main()
