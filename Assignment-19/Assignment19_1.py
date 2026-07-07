power = lambda No : No**2

def main():

    print("Enter the Number : ")
    Number = int(input())

    ret = power(Number)
    print(f"Power of 2 of {Number} is = {ret}")


if __name__=="__main__":
    main()

'''
OUTPUT:
1. Enter the Number :
   4
   Power of 2 of 4 is = 16

2. Enter the Number :
   6
   Power of 2 of 6 is = 36
    

'''