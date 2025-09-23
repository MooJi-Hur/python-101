from datetime import datetime
from time import sleep

# 파라미터로 들어온 함수가 실행된 순서를 살펴보는 예제
def my_logger(func):
    def logging():

        print(f"[pre-logger] : {datetime.now()}")
        func()
        print(f"[post-logger] : {datetime.now()}")

    return logging # logging()

# my_logger는 greeting이라는 함수를 인자로 받음
# @my_logger
def no_deco_greeting():
    sleep(2)
    print("Hello, world!")

@my_logger
def deco_greeting():
    sleep(2)
    print("Hello, world!")

if __name__ == "__main__":
    my_logger(no_deco_greeting)()
    deco_greeting()
