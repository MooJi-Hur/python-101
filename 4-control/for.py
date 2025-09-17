# for 변수 in collections :
# collections : list, tuple, set, dict, ...
# iterable -> __iter__, __next__ 순환

subjects = ["python", "ds", "de"]

for sub in subjects : ## __next__를 이용
    print(sub)

for i in range(1, 101): # range : 시작 값과 끝 값을 가지고 있고, 사용할 때 메모리에 값이 만들어짐
    print(i, end=", ")
print()

# 중첩
for i in range(1, 10) :
    print(i)
    for j in range(1, 10):
        print(f"{i}, {j}")
    print("\n")

# 구구단 출력
for i in range(1, 10) :
    print(i)
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")
    print("\n")