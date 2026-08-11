import datetime
import os
import schedule
import sys
import time


def monitor_file_size():
    filename = "DemoX.txt"
    log_file = "FileSizeLog.txt"

    fobj = open(log_file, "a")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if os.path.exists(filename):
        file_size = os.path.getsize(filename)
        absolute_path = os.path.abspath(filename)

        fobj.write(f"File path: {absolute_path}\n")
        fobj.write(f"File size in bytes: {file_size}\n")
        fobj.write(f"Date and time: {timestamp}\n")
        print(f"Logged size for {filename}: {file_size} bytes")
    else:
        fobj.write(f"Error: The file '{filename}' does not exist at {timestamp}.\n")
        
    fobj.write("-" * 40 + "\n")
    fobj.close()


def main():
    border = "-" * 40

    print(border)
    print("Marvellous Automation Script - Assignment 2")
    print(border)


    schedule.every(30).seconds.do(monitor_file_size)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
