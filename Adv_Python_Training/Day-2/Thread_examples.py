import time
import threading

def worker(sleeptime):
    print(threading.current_thread().getName(), "entering")
    time.sleep(sleeptime)
    print(threading.current_thread().getName(), "exiting")

if __name__ == '__main__':

    print("sequentially")
    worker(2)
    print ( "Now Parallely ")
    ths = []
    st = time.time()
    for i in range(10):
        t = threading.Thread(target=worker, args=(5,))
        ths.append(t)
    [t.start() for t in ths]
    [t.join() for t in ths]  # wait for t to end
    print("Time taken", round(time.time() - st, 3), "secs")