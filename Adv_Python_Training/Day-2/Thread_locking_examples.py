import time
import threading

shared = []
def worker(sleeptime, lock):
    global shared
    print(threading.current_thread().getName(), "entering")
    with lock:
        print(threading.current_thread().getName(), "lock Acquired")
        time.sleep(sleeptime)
        shared.append(threading.current_thread().getName())
    time.sleep(2)
    print(threading.current_thread().getName(), "exiting")

if __name__ == '__main__':
    lock = threading.Lock()
    #lock = threading.Semaphore(2) # 2 threads will take a lock simultaniously
    ths = []
    st = time.time()
    for i in range(10):
        t = threading.Thread(target=worker, args=(5,lock))
        ths.append(t)
    [t.start() for t in ths]
    [t.join() for t in ths]# wait for t to end
    print("Time taken", round(time.time()-st, 3), "secs")