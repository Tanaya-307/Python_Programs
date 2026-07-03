def Sum_of_digits(No):
    sum = 0

    while No > 0:
        res = No % 10
        sum += res
        No = No // 10
    print("sum of Digits is : ",sum)

def main():
    print("Enter the Number : ")
    Num = int(input())
    Sum_of_digits(Num)
    

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the Number :
123
sum of Digits is :  6

'''

