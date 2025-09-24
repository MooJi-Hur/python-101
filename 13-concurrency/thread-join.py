from threading import Thread

value = 0

def calc(name, start, end):
    result = 0
    for i in range(start, end):
        result += i
        print(f"{name}: {i}")

    print(f"{name} sum: {result}")

    global value
    value += result

if __name__ == '__main__':
    print("Main thread started")

    first_thread = Thread(target=calc, args=("first", 1, 50))
    second_thread = Thread(target=calc, args=("second", 50, 101))

    first_thread.start()
    second_thread.start()

    # 아래 코드가 없으면 동일한 value를 여러 쓰레드에서 함께 사용하여 결과가 다를 수 있음
    # 전역 변수 결과를 조인
    first_thread.join()
    second_thread.join()


    print(f"result = {value}")