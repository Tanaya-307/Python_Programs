Divisible = lambda no:no if(no % 3 ==0 and no % 5==0)else()

def main():
    lst = []

    print("Enter list : ")
    
    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)

    no = int (input())
    lst.append(no)


    print(lst)

    print("Input data is : ",lst)

    Fdata = list(filter(Divisible,lst))

    print("List of Numbers divisible by 3 and 5 : ",Fdata)

    
if __name__=="__main__":
    main() 

'''
OUTPUT:
12
30
15
60
55
[12, 30, 15, 60, 55]
Input data is :  [12, 30, 15, 60, 55]
List of Numbers divisible by 3 and 5 :  [30, 15, 60]
'''
