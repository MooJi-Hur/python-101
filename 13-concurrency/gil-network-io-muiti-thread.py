from threading import Thread
from datetime import datetime
import urllib.request

# io, network 작업에서는 multi thread가 유리

def my_logger(func):
    def logging():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"[time] : {end - start}")

    return logging

def crawling(name):
    with urllib.request.urlopen("https://www.google.com") as response:
        html = str(response.read())
        with open(f"{name}-url", "a") as f:
            f.write(html)


@my_logger
def func_way():
    for i in range(10):
        crawling("func")

@my_logger
def thread_way():
    threads = [Thread(target=crawling, args=("thread",)) for _ in range(10)]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    func_way()
    thread_way()


