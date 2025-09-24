from threading import Thread
from datetime import datetime

def my_logger(func):
    def logging():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"[time] : {end - start}")

    return logging

def calc(name):
    result = 0

    for i in range(1000000):
        result += i

    with open(f"{name}.txt", "w") as f:
        f.write(str(result) + "\n")

@my_logger
def func_way():
    for i in range(10):
        for i in range(10):
            calc("func")

@my_logger
def thread_way():
    threads = [Thread(target=calc, args=("thread", )) for _ in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    func_way()
    thread_way()