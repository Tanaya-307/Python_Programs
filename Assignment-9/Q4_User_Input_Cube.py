def Cube(No):

    result = No **3 
    print("Cube of",No,"is :",result)

def main():

    print("Enter the Number : ")
    Number = int(input())

    Cube(Number)

if __name__=="__main__":
    main()

'''
#OUTPUT:
Enter the Number :
7
Cube of 7 is : 343

'''

