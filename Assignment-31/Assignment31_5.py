import sys
import os
import datetime
import schedule
import time

def directory_scanner():

    directorypath = "Marvellous"
    filecount = 0 
    subdir_count = 0

    directorypath = os.path.abspath(directorypath)

    for foldername,subfolder,filename in os.walk(directorypath):
        
        for fname in filename:
           filecount = filecount + 1
    fobj = open("DirectoryCountLog.txt","a")
    fobj.write(f"\nDirectory path: {directorypath}\n")
    fobj.write(f"Total Files : {filecount}\n")
    fobj.write(f"Scan time : {datetime.datetime.now()}\n")

        
def main():
    border = "-"*40

    print(border)
    print("Marvellous Automation Script")
    print(border)

    schedule.every(5).minutes.do(directory_scanner)
    
    while True : 
        schedule.run_pending()
        time.sleep(1)

    print()
    print(border)
    print("Thank you for using Marvellous Automation Script")
    print(border)


if __name__ =="__main__" :
    main()