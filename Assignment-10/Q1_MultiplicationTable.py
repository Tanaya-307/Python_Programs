def Multiplication_Table(No):
    for i in range(1,11):
        res = No * i
        print( No,"x",i,"=",res)

def main():

    print("Enter the Number :")
    Num = int(input())
    print("Multiplication Table of",Num,"is :\n")
    

    Multiplication_Table(Num)

if __name__=="__main__":
    main()


'''
OUTPUT: 
Enter the Number :
4
Multiplication Table of 4 is :

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20
4 x 6 = 24
4 x 7 = 28
4 x 8 = 32
4 x 9 = 36
4 x 10 = 40
'''
