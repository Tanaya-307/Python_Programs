def pattern(No):
    for i in range(1,No+1):
        print("* " * No)

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
* * * * *
* * * * *
* * * * *
* * * * *
'''