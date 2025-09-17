# 형 변환
a = int(1.2)
print(a)

b = int('12')
print(b)

# c = int("1.2")    # 실수 형태의 문자열은 형변환이 되지 않음 -> 실수 생성자가 따로 있으므로. float
# print(c)

print(int('1111', 2))
print(int('77', 8))

# print(int(77, 8)) TypeError: int() can't convert non-string with explicit base

print(int(2))
print(int(True))
print(bool(2))
print(int(False))

print(float("12.5"))

