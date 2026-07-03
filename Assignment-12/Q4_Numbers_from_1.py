def printNumber(No):

    for i in range(1, No + 1):
        print(i)

def main():
    print("Enter the Number : ")
    No1 = int(input())
    printNumber(No1)
    
if __name__=="__main__":
    main()