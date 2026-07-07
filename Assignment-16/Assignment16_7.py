def Divisibleby_5(No):

    if No % 5 == 0:
        return True
    
    return False

def main():

    print("Enter the number : ")
    Number = int(input())

    ret = Divisibleby_5(Number)
    print(ret)


if __name__=="__main__":
    main()

'''
OUTPUT:
1 . Enter the number :
    8
   False

2 . Enter the number :
    25
    True
'''