def printNumber(No):

    for i in range(No,0,-1):
        print(i)

def main():
    print("Enter the Number : ")
    No1 = int(input())
    print("Reversed Numbers are : ")
    printNumber(No1)
    
if __name__=="__main__":
    main()