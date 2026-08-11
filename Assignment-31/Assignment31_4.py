import sys
import os
import time
import datetime
import schedule

def directory_scanner(directorypath):
    now = datetime.datetime.now()
    timestamp_content = now.strftime("%d-%m-%Y %I:%M:%S %p")
    timestamp = time.ctime()
    logfilename = "Marvellous%s.log"%(timestamp)
    logfilename = logfilename.replace(" ","_")
    logfilename = logfilename.replace(":","_")

    print("Log file gets created with name :",logfilename)
    fobj = open(logfilename,"w")

    fobj.write("Log file Created successfully\n")
    fobj.write(f"Creation time :{timestamp_content}")

    for foldername,subfolder,filename in os.walk(directorypath):
         for fname in filename:
            fobj.write(fname + "\n")
   

    fobj.close()
    
    

def main():
    border = "-"*40

    print(border)
    print("Marvellous Automation Script")
    print(border)

    if (len(sys.argv)==2):

        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This automation script is used to travel the directory ")
            print("For better usage use --u")
        
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
             print("plz execute the script as ")
             print("pyton Filename.py Directoryname")
             print("directory name should e absolute path")
        else:
           directory_scanner(sys.argv[1])

        schedule.every(2).seconds.do(directory_scanner, directorypath=sys.argv[1])

        while True : 
             schedule.run_pending()
             time.sleep(1)
           
    else:
        print("invalid input")
        print()

    print("Automation script started")
    
    

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
Log file gets created with name : MarvellousFri_Jul_24_21_33_10_2026.log
'''