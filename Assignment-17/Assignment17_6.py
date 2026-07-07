def pattern(No):
    for i in range(No,0,-1):
        print("* " *i)

def main():
    value = int(input("Enter the input :"))
    print("Input is :",value)

    pattern(value)

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the input :5
Input is : 5
* * * * *
* * * *
* * *
* *
*
'''