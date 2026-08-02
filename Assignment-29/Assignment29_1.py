import os

def main():
    file_name = input("Enter the Filename : ")
    ret = os.path.exists(file_name)

    if (ret == True):
        print("File is present in current directory ")
    else:
        print("There is no such file")

if __name__=="__main__":
    main()
'''
OUTPUT:
Enter the filename : demo.txt
File exists in the directory

'''
