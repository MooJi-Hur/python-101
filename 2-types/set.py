# set : 순서 x, 중복 x

a = {"1", "2", "4", "4"}
print(a) # 출력할 때마다 순서가 다르며, 고유한 값만 남겨둠
print(type(a))

# 숫자는 정렬됨 - 숫자는 해싱할 때 숫자 자체가 주소값으로 저장됨
b = {1, 5, 4}
print(b)
print([hash(x) for x in [1, 2, 3, 4, "5"]])

# set()
c = set([1, 2, 3, 4])
print(c)

d = set("1 2 3 4")
print(d)

c.add(6)
print(c.add(6)) # 사용자에게 돌려줄 값이 없으므로 None을 반환
print(c)
print(c.pop())
print(c) # 숫자형 값을 넣었을 때, 정렬이 되고, 앞의 값부터 빠짐 # 리스트는 뒤에서 빠짐


#set()안에 반복가능한 객체를 넣으면 어떻게 되는가?
d = set("hello, world!") # 순서가 없고, 중복이 없는 원소로 분해됨
print(d)

left = {'a', 'b', 'c', 'd'}
right = {'c', 'd', 'e', 'f'}

# union한 결과가 같아서 연산한 결과를 그대로 가져옴
print(left.union(right))
print(left | right)

# 교집합
print(left.intersection(right))
print(left & right)

# 차집합
print(left.difference(right))
print(left - right)

# frozenset 변경이 불가능한 set
e = frozenset({1, 2, 3, 4, 5})
print(e)
# e.pop() 불가능

print(dir(set))
print(dir(frozenset))

print(type(set(e)))

