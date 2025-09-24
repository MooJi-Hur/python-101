from threading import Thread
from time import sleep

value = 10

def calc(name, num, sleep_time):
    global value    # 함수 외부의 자원을 사용 # 여러 쓰레드가 하나의 변수를 함께 쓰고 있음
    for i in range(10):
        value = value + num
        print(f"{name} {i}: {value}\n")
        sleep(sleep_time)

if __name__ == '__main__':
    print("Main thread started!")

    # arg에는 iterable한 객체면 됨, 튜플도
    my_thread = Thread(target=calc, args=["my", 1, 1])
    # daemon 은 코드를 모두 실행하지 않아도 다른 쓰레드가 종료되면 함께 정리됨
    daemon_thread = Thread(target=calc, args=["daemon", -1, 0.5])

    # daemon thread : thread를 보조하는 thread, daemon이 아닌 thread가 더이상 없을 때 종료
    daemon_thread.daemon = True

    my_thread.start()
    daemon_thread.start()


    print(f"my_Thread : {my_thread.daemon}\n")
    print(f"daemon_Thread : {daemon_thread.daemon}\n")

    print(f"my_Thread : {my_thread.is_alive()}\n")
    print(f"daemon_Thread : {daemon_thread.is_alive()}\n")


    print("Main thread finished!")

