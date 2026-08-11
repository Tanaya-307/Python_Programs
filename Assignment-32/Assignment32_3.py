import sys
import os
import datetime
import schedule
import time

def display_file():
    filename = "demo.txt" 
    scan_time = datetime.datetime.now().strftime("%H:%M:%S %p")
    
    print(f"\n--- Reading file at {scan_time} ---")
    
    if not os.path.exists(filename):
        print("Error: File does not exist")
        return
        
    if os.path.getsize(filename) == 0:
        print("Notice: File is empty")
        return
        
    try:
        fobj = open(filename, "r")
        print(fobj.read())
        fobj.close()
    except PermissionError:
        print("Error: Permission is denied")
    except Exception:
        print("Error: File cannot be opened")

def main():
    border = "-" * 40
    
    print(border)
    print("Marvellous Automation Script")
    print(border)
    
    schedule.every(1).minutes.do(display_file)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
    print()
    print(border)
    print("Thank you for using Marvellous Automation Script")
    print(border)

if __name__ == "__main__":
    main()