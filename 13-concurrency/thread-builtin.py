from threading import Thread

"""
thread : 프로세스 내부 작업 단위
process : program을 실행하여 메모리에 실제로 적재된 구현체 (job, task)
program : 코드로 이루어진 실행 가능한 파일
"""

# class에서 run에 해당하는 부분 thread를 실행한 뒤의 동작 내용을 정의
def bark(name, message):
    for i in range(10):
        print(f"{name}: {message} ({i}번째)")


if __name__ == '__main__':  # 메인 쓰레드 실행

    # 컴퓨터 자원에는 하나의 쓰레드만 접근 가능
    # 스케쥴러는 어떤 쓰레드가 접근할지 정함
    # 컨텍스트 스위칭 : 자원에 접속하는 쓰레드를 변경
    first_thread = Thread(target=bark, args=("first_dog", "멍멍"))
    second_thread = Thread(target=bark, args=("second_dog", "왈왈"))
    third_thread = Thread(target=bark, args=("first_cat", "야옹"))
    fourth_thread = Thread(target=bark, args=("second_cat", "애옹"))

    # start = run 호출
    # 실행할 때마다 출력 순서가 다름
    first_thread.start()
    second_thread.start()
    third_thread.start()
    fourth_thread.start()

    print("End!")

