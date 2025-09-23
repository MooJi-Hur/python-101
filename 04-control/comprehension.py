#
list01 = list()
for i in range(1, 11):
    list01.append(f"a{i}")

print(list01)   # 원소 모두 출력해줌

list02 = [f"a{i}" for i in range(1, 11)]    # list 객체를 만들 때 반복문을 활용
print(list02)

# 1 ~ 10 사이의 짝수만 list
listEven = [f"a{i}" for i in range(2, 11, 2)]
print(listEven)

listEven = [i for i in range(1, 11) if i % 2 == 0]  # 조건문 추가
print(listEven)

subjects = [
    "python", "analysis", "database",
    "html", "css", "javascript",
    "django", "science", "engineering"
]
print(subjects)

# subjects item 중 a를 포함하고 있는 item만 새로운 list로 만들자

subjects_a = [name for name in subjects if 'a' in name]
print(subjects_a)


# 중첩
# [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]

grid = [[ j + i for j in range(4)] for i in range(0, 15, 4)]
print(grid)

grid = [[4 * i + j for j in range(4)] for i in range(4)]





