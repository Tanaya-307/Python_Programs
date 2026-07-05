Cube=lambda No : No**3

def main():

    print("Enter the Number : ")
    Number = int(input())

    ret = Cube(Number)
    print(f"Cube of {Number} is = {ret}")


if __name__=="__main__":
    main()

'''
Output :
Enter the Number :
2
Cube of 2 is = 8
'''