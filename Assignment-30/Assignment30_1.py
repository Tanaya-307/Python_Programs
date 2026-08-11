import schedule
import time
import datetime

def display():
    print("jay Ganesh...")

def main():
    print("Automation script started")

    schedule.every(2).seconds.do(display)

    while True : 
        schedule.run_pending()
        time.sleep(1)

    print("End of automation script")


if __name__=="__main__":
    main()

'''
OUTPUT:
Automation script started
jay Ganesh...
jay Ganesh...
jay Ganesh...
jay Ganesh...
'''