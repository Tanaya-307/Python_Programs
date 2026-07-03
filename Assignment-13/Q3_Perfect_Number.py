def perfect_num(No):
    sum = 0

    for i in range(1,No):
        if(No % i == 0 ):
            sum += i       # sum of all divisors of Number
    
    if (sum == No):        # if sum of all divisors == num, it is perfect
        print("It is a perfect number")
    else :
        print("It is not a perfect number")


def main():
    print("Enter the Number : ")
    Num = int(input())
    perfect_num(Num)
    

if __name__=="__main__":
    main()