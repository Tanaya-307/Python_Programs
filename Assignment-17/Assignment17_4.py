def sum_factors(No):
    sum = 0
    for i in range(1,No):
        if (No % i == 0):
            sum = sum + i
    return (sum)
        
def main():
    print("Enter the Number : ")
    Num = int(input())

    Res = sum_factors(Num)

    print(f"Addition  of factors of {Num} is : {Res}")
if __name__=="__main__":
    main()