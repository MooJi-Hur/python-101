
# 변수에 값을 대입했을 때, 값이 변화는지의 여부에 따라 타입을 나눴음
# 값을 저장하고, 복사하는 방식과 관련이 있음

# mutable : list, set, dictionary
# immutable : numbers, tuple, str, frozenset

a = [1, 2, 3, 4, 5] # 아이템들의 주소값을 저장
print(a)
print(id(a))

a.append(6)
print(a)
print(id(a)) # 첫 원소 값의 주소를 담고 있으므로 값을 추가해도 주소값이 변하지 않음

b = 10
print(b)
print(id(b))

f = 10
print(f)
print(id(f))

b = 11
print(b)
print(id(b))    # b는 10이 담긴 주소값을 가지고 있다가 20이 담긴 주소값으로 내용을 바꿈

c = (1, 2, 3, 4, 5)
print(c)
print(id(c))
print(id(c[0]))

c = c + tuple(a)
print(c)
print(id(c))    # 튜플까지 전체를 새로 만들어서 주소값 시작점을 담음

