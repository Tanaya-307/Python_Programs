def PrintEven():
    count = 2
    Num = 0

    while Num <= 9:

        if (count % 2==0):

            print(count,end=" ")
            Num = Num + 1
        count = count + 1
    

def main():
     print("First 10 Even Numbers are : ")
     PrintEven()

if __name__=="__main__":
    main()

'''
OUTPUT:
First 10 Even Numbers are :
2 4 6 8 10 12 14 16 18 20 22
'''



            