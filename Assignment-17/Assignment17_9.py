def count_digit(Num):
    count = 0

    while Num > 0:
        Num //=10 
        count =count + 1
    print("Total digits : ",count)
    
def main():
    print("Enter the Number : ")
    No = int(input())
    count_digit(No)

if __name__=="__main__":
    main()

'''
OUTPUT:

Enter the Number :
5187934
Total digits :  7

'''
