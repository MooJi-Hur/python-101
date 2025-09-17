# while 조건:
# 조건이 True인 동안 반복

i = 1

while i <= 10:  # 10까지 출력, 조건이 참인 동안 구문 반복
    print(i)
    i += 1

my_sum = 0
my_count = 1

while my_count <= 10:
    my_sum += my_count
    my_count += 1
else:   # while 조건문에 대한 else를 사용할 수 있음, else 위 구문이 정상 종료되면 else 이하 실행
        # while 내 if 문이 있을 경우에는 다음 else는 depth로 구분
    print(f"sum : {my_sum} \t count : {my_count}")

