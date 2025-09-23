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


# hello, world를 10번 반복해서 출력

for _ in range(10):
    print("hello, world!")

# enumerate : (index, value)
print(subjects)

for idx, val in enumerate(subjects):    # index 정보를 함께 출력
    print(f"index : {idx} \t value : {val}")

print(enumerate(subjects))  # subjects를 활용한 새 객체를 만들어 반환
print(id(enumerate(subjects)))

for i in enumerate(subjects):   # tuple이 출력됨, unpacking 한 것
    print(i)


