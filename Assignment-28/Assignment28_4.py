def main():
    Filename1 = input("Enter 1st file  to open : ")
    Filename2 = input("Enter 2nd File to copy the contents : ")
    
    fobj1= open(Filename1,"r")
    fobj2 = open(Filename2,"w")

    for lines in fobj1:
        contents = fobj1.read()
        fobj2.write(contents)
        
    print(f"Contents Copied to {Filename2}")

    fobj1.close()
    fobj2.close()


if __name__ == "__main__":
    main()

'''
OUTPUT:
Enter 1st file  to open : Assignment28_1.py
Enter 2nd File to copy the contents : demo.txt
Contents Copied to demo.txt
'''