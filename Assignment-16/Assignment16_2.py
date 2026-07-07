def ChkNum(Num):
    if (Num % 2 == 0):
        print(f"{Num} is Even Number")
    else:
        print(f"{Num} is Odd Number")

def main():
    print("Enter the Number : ")
    no = int(input())

    ChkNum(no)
    

if __name__=="__main__":
    main()

'''
OUTPUT:
1.Enter the Number :
  11
  11 is Odd Number

2.Enter the Number :
  8
  8 is Even Number

'''