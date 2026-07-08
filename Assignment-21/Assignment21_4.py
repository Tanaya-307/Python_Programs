import threading
 
def Sumvalue(data,results):
    Sum = 0
    for no in data:
        Sum = Sum + no

    results['Sum'] = Sum

def Product(data,results):
    product = 1
    for no in data:
        product = product * no

    results['product'] = product

def main():
    print("Enter the number of elements :")
    n = int(input())

    elements=[]
    print(f"Enter {n} elements")
    

    for i in range (n):
        value = int(input())
        elements.append(value)
    print(f"list :{elements}")

    results={}

    t1=threading.Thread(target =Sumvalue,args=(elements,results))
    t2=threading.Thread(target =Product,args = (elements,results))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    print(f"sum of list is :{results.get('Sum')}")
    print(f"product of list is :{results.get('product')}")

    print("Exit from main")

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
sum of list is :10
product of list is :24
Exit from main
'''