# tuple : list와 유사하나 수정을 할 수는 없음

# tuple을 만드는 방법 총 세 가지

# literal : 값을 이용해 객체를 만듦
# (값, 값, 값, ...)
a = (1, 2, 3, 4, 5)
print(a)
print(type(a))

# 생성자를 이용해 명시적으로 객체를 만듦
b = tuple([5,6,7,8])
print(b)
print(type(b))

# a.append(6) AttributeError: 'tuple' object has no attribute 'append'
print(a)
print(type(a))


print(dir(list))
print(dir(tuple))
print(a.count(3)) # 해당 값이 몇 개 있는지 확인하는 기능


c = a + b # 새로운 튜플을 만들었음 즉, a와 b를 참조하는 새로운 c를 할당
print(c)
print(type(c))

print(a+a*2)

# 형 변환
d = list(c)
print(d)
print(type(d))
d.remove(3)
print(d)

# list -> tuple
e = tuple(d)
print(e)
print(type(e))
# 모델이 튜플을 사용하는 경우가 있음

# packing
f = 1, 2, 3
print(f)
print(type(f))

# unpacking
g, h, i = f
print(g)
print(h)
print(i)

# j, k = f # ValueError: too many values to unpack (expected 2)
# print(j)
# print(k)
# print(type(j))
# print(type(k))

j = f   # 이것도 언팩킹
print(j)
