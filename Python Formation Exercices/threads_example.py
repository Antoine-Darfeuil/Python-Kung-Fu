from threading import *
import time, random

class MyThread(Thread):
    index = 0
    lock = Lock()

    def __init__(self, message):
        super().__init__()
        self._message = message

    def run(self):
        '''Methode héritée re-définie.'''
        for n in range(1, 100):
            time.sleep(0.2)
            # MyThread.lock.acquire()
            # print(self._message, MyThread.index)
            # MyThread.index += 1
            # MyThread.lock.release()
            with MyThread.lock:
                print(self._message, MyThread.index)
                MyThread.index += 1


class Buffer:

    def __init__(self):
        self._lock = RLock()
        self.data = []

    def put(self, n):
        with self._lock:
            self.data.insert(0, n)

    def get(self):
        with self._lock:
            if len(self.data) == 0:
                return None
            return self.data.pop()
        

class Producer(Thread):

    def __init__(self, buffer):
        super().__init__()
        self._buffer = buffer

    def run(self):
        for n in range(20):
            time.sleep(random.randint(1, 10) / 100)
            self._buffer.put(n)
    

class Consumer(Thread):

    def __init__(self, buffer):
        super().__init__()
        self._buffer = buffer
        
    def run(self):
        for n in range(30):
            time.sleep(random.randint(1, 10) / 100)
            item = self._buffer.get()
            if not item == None:
                print(item)
    



if __name__ == '__main__':

    buff = Buffer()
    prd = Producer(buff)
    csm = Consumer(buff)
    prd.start()
    csm.start()

    prd.join()
    csm.join()
    
    


    
    
    mt1 = MyThread("A")
    mt1.start()

    mt2 = MyThread("     B")
    mt2.start()

    mt1.join()
    mt2.join()
    print("mt1 et mt2 fini")
