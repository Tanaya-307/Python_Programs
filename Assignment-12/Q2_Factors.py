def print_factors(No):

    for i in range(1,No+1):
        if (No % i == 0):
            print(i)
        
def main():
    print("Enter the Number : ")
    Num = int(input())
    print("Factors of ",Num,"are :")
    print_factors(Num)
    

if __name__=="__main__":
    main()

'''
Enter the Number :
12
Factors of  12 are :
1
2
3
4
6
12
'''