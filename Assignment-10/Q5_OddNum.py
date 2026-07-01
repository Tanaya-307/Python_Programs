def OddNumbers(Num):
    for i in range(1,Num+1):

        if i % 2 != 0:
            print(i)

def main():
    print("Enter the Number : ")
    no = int(input())
    print("All Odd Numbers upto",no,"are : ")

    OddNumbers(no)

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the Number :
10
All Odd Numbers upto 10 are :
1
3
5
7
9
'''