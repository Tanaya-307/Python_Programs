square=lambda No : No**2

def main():

    print("Enter the Number : ")
    Number = int(input())

    ret = square(Number)
    print(f"square of {Number} is = {ret}")


if __name__=="__main__":
    main()

    '''
    Enter the Number :
    2
    square =  4
    '''