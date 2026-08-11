import sys
import os
import datetime

def directory_scanner():

    directorypath = "Marvellous"
    filecount = 0 
    subdir_count = 0

    directorypath = os.path.abspath(directorypath)

    for foldername,subfolder,filename in os.walk(directorypath):

        for sname in subfolder:
            subdir_count = subdir_count + 1
        
        for fname in filename:
           filecount = filecount + 1

    print("\nDirectory path : ",directorypath)
    print("Total Files :",filecount)
    print("Total Subdirectories: ",subdir_count)
    print("Scan time : ",datetime.datetime.now())

        
def main():
    border = "-"*40

    print(border)
    print("Marvellous Automation Script")
    print(border)

    directory_scanner()

    print()
    print(border)
    print("Thank you for using Marvellous Automation Script")
    print(border)


if __name__ =="__main__" :
    main()

'''
OUTPUT:

----------------------------------------
Marvellous Automation Script
----------------------------------------

Directory path :  C:\Users\Shree\Desktop\python\Marvellous
Total Files : 13
Total Subdirectories:  3
Scan time :  2026-07-24 20:48:24.427111

----------------------------------------
Thank you for using Marvellous Automation Script
----------------------------------------
'''