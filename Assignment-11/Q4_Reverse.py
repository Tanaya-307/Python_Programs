def reverseNum(No):

    Num = 0

    while (No > 0):
        Num = (Num*10) + (No%10)
        No = No // 10
    return Num 
    
def main():
    print("Enter the Number : ")
    Number = int(input())

    ret = reverseNum(Number)
    print("Reverse Num is ",ret)

    
if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the Number :
123
Reverse Num is  321
'''