from threading import Thread
from datetime import datetime

value = 100000000
result = 0


def calc(name, start, end):
    count = 0
    for i in range(start, end):
        count += i

    print(f"{name}: {count}")

    global result
    result += count

def single_thread():
    start = datetime.now()

    global value
    global result

    result = 0

    first_thread = Thread(target=calc, args=["single_thread", 1, value + 1])

    first_thread.start()
    first_thread.join()

    print(f"result: {result}")
    end = datetime.now()

    print(f"single thread time: {end - start}")


def multi_thread():
    start = datetime.now()

    global result
    result = 0

    first_thread = Thread(target=calc, args=["multi_thread", 1, value // 2])
    second_thread = Thread(target=calc, args=["multi_thread", value // 2, value + 1])

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()

    print(f"result: {result}")
    end = datetime.now()

    print(f"multi thread time: {end - start}")


if __name__ == "__main__":

    # 시간 차이가 크지 않음
    # GIL : Global Interpreter Lock
    single_thread()
    print("---")
    multi_thread()
    print("---")
