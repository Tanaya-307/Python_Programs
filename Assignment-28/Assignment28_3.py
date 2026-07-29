def main():
    Filename = input("Enter Filename : ")
    fobj = open(Filename,"r")
    print(f"Lines in {Filename} are :")

    for lines in fobj:
          print(lines)
        

    fobj.close()


if __name__ == "__main__":
    main()

'''
OUTPUT:
Enter Filename : DemoX.txt
Lines in DemoX.txt are :
Jay Ganesh...
'''