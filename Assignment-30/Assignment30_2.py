import schedule
import time
import datetime

def display():
    print("Current Date and Time : ",datetime.datetime.now())

def main():
    print("Automation script started")

    schedule.every(1).minutes.do(display)

    while True : 
        schedule.run_pending()
        time.sleep(1)

    print("End of automation script")


if __name__=="__main__":
    main()

'''
OUTPUT:
Automation script started
Current Date and Time :  2026-07-22 11:39:16.304357
Current Date and Time :  2026-07-22 11:40:16.355059
Current Date and Time :  2026-07-22 11:41:16.406567
'''