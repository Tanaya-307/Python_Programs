def length(name):
    count = 0
    for i in name:
        count = count + 1
    print(count)

def main():
   string = input("Enter the Name : ")
   length(string)
   

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the Name : Marvellous
10
'''