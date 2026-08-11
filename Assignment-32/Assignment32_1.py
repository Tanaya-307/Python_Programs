import sys
import os
import datetime
import schedule
import time

def create_file():

    
    filestamp = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S_%p")
    filename = f"file_{filestamp}.txt"
    fobj = open("filename.txt","w")
    fobj.write(f"Filename is :{filename}\n")
    creation_date = datetime.datetime.now().strftime("%d-%m-%Y")
    fobj.write(f"Creation Date  : {creation_date}\n")
    scan_time = datetime.datetime.now().strftime("%H:%M:%S %p")
    fobj.write(f"Scan time : {scan_time}\n")
    
def main():
    border = "-"*40

    print(border)
    print("Marvellous Automation Script")
    print(border)
    
    schedule.every(3).seconds.do(create_file)
    
    while True : 
        schedule.run_pending()
        time.sleep(1)

    print()
    print(border)
    print("Thank you for using Marvellous Automation Script")
    print(border)
    


if __name__ =="__main__" :
    main()