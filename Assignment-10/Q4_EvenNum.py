def EvenNumbers(Num):
    for i in range(1,Num+1):

        if i % 2 == 0:
            print(i)

def main():
    print("Enter the Number : ")
    no = int(input())
    print("All Even Numbers upto",no,"are : ")

    EvenNumbers(no)

if __name__=="__main__":
    main()


'''
OUTPUT:
Enter the Number :
10
All Even Numbers upto 10 are :
2
4
6
8
10
'''