def pattern(No):
    print("* "*No,end=" ")

def main():
    print("Enter the Number : ")
    value = int(input())

    pattern(value)

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the Number :
5
* * * * *
'''