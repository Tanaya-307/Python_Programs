import schedule
import time

def display(msg):
    print(msg)

    
def main():
   msg = input("Enter message : ")
   interval = int(input("Enter time interval : "))

   schedule.every(interval).seconds.do(display,msg)

   while True : 
        
        schedule.run_pending()
        time.sleep(1)

    

if __name__=="__main__":
    main()

'''
OUTPUT:
Enter message : Jay Ganesh
Enter time interval : 2
Jay Ganesh
Jay Ganesh
Jay Ganesh
'''