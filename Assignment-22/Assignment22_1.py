import multiprocessing

def Sum_of_squares(No):
       sum = 0
       for i  in range(1,No+1):
              sum = sum + (i*i)
       return sum
       
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

    pobj=multiprocessing.Pool()

    Result = pobj.map(Sum_of_squares,Data)

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
10000000
20000000
30000000
40000000
list :[10000000, 20000000, 30000000, 40000000]
Result is
[333333383333335000000, 2666666866666670000000, 9000000450000005000000, 21333334133333340000000]

'''