# 한 줄 주석
"""
여러 줄 주석
"""

a = 1   # 변수 대입 값
print(a)
print(type(a))


"""
singleton 구조
- 동일한 None 주소 값을 참조하고 있음
"""


b = None    # 다른 언어의 null에 해당하는 타입
print(b)
print(type(b))

c = None
print(c)

print(id(c))
print(id(b))