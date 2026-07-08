import threading

def function(count,Lock):

    Lock.acquire()
    count[0]=count[0]+100
    Lock.release()

    print(count)

def main():
    count = [100]
    Lock = threading.Lock()

    print(count)


    t1=threading.Thread(target =function,args=(count,Lock))
    t2=threading.Thread(target =function,args=(count,Lock))

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

if __name__=="__main__":
    main()