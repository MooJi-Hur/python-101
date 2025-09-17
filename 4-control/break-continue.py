# break : 반복문을 종료하고 다음 명령 수행
i = 1

while i <= 10:
    if i > 5:
        break
    print(i, end="")
    i += 1

print("end!!!")

# continue : 아래의 코드를 무시하고 다음 반복으로 진행
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print("end!!!")