def Sum(N):
    sum = 0
    for i in range(1,N+1):
        sum = sum + i
    print("sum of first ",N,"natural numbers is :",sum)

def main():
    print("Enter the value of N ")
    no = int(input())
    Sum(no)

if __name__=="__main__":
    main()

'''
OUTPUT:

Enter the value of N
5
sum of first  5 natural numbers is : 15

'''
