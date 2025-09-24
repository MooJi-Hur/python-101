from threading import Thread, Lock
from time import sleep

# thread가 공유할 자원
resource = 0

def increase_resource():
    global resource
    resource += 1

class LockThread(Thread):
    def __init__(self, name, lock):
        Thread.__init__(self)
        self.name = name
        self.lock = lock

    def run(self):
        global resource
        resource = 0    #

        for i in range(10):
            # lock.acquire : 잠금
            self.lock.acquire()
            increase_resource()
            sleep(0.5)

            # lock.release
            self.lock.release()

            print(f"{self.name} {i} : {resource}")


if __name__ == "__main__":
    # Lock : 특정 Thread가 resource에 접근할 경우, 다른 Thread는 그 리소스에 접근 불가
    lock = Lock()
    thread_list = [
        LockThread("Thread-1", lock),
        LockThread("Thread-2", lock),
        LockThread("Thread-3", lock),
        LockThread("Thread-4", lock),
        LockThread("Thread-5", lock),
    ]

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print(resource)

