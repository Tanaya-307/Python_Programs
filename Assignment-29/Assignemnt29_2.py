import os

def main():
    filename = input("Enter the Filename : ")
    fobj = open(filename,"r")
    ret = fobj.read()
    print("\n------Contents of file are : -------\n")
    print (ret)
    print("\n------ contents end here -------\n")

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter the Filename : demo.txt

------Contents of file are : -------

    Filename = input("Enter Filename : ")
    fobj = open(Filename,"r")

    count = 0

    for lines in fobj:
        count = count + 1

    fobj.close()

    print(f"Total Number of lines in {Filename} are : {count}")

if __name__ == "__main__":
    main()

OUTPUT:
Enter Filename : Assignment28_1.py
Total Number of lines in Assignment28_1.py are : 15


------ contents end here -------

'''