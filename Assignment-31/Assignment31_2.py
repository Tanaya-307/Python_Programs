import schedule
import time

def displaymessage(msg):
    print(msg)

    
def main():
   msg = input("Enter message : ")
   schedule.every(5).seconds.do(displaymessage,msg)

   while True : 
        
        schedule.run_pending()
        time.sleep(1)

    

if __name__=="__main__":
    main()
