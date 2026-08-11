import datetime
import schedule
import time

def display():
         
    fobj = open("MarvellousX.txt","a")
    print("File gets opened")

    fobj.write(print("Task executed at : ",datetime.datetime.now()))

    fobj.close

def main():
    print("Automation script started")
    
    schedule.every(1).minutes.do(display)

    while True : 
        schedule.run_pending()
        time.sleep(1)

    

if __name__=="__main__":
    main()

   

