# sequence : 순서가 있는 값들을 가진 객체
# 변수 명을 여러 개 지어야하는 불편함을 덜어줌
# list : 순서 o, 중복 o
# [값, 값, 값]
a = [5, 3, 4, 2, 3, 1, 3]
print(a)
print(type(a))

a.append(6)
print(a)

#list() 생성자
b = list()
print(b)
print(type(b))

b.append(6)
b.append(7)
b.append(8)
print(b)

# list[index]
print(a[2])
print(b[1])


# dir : 객체의 속성, 메서드 확인
# __??__ : special method (magic method)
# __iter__ : 반복자
print(dir(list))
print(dir(list()))

b.reverse()
print(b)

print(a)
print(a.pop())
print(a)

# a.append() <- .은 참조 연산자로 리스트 클래스의 함수
c = a + b
print(len(c))
print(type(c))

print(a)
print(a * 2)    # list가 두 번 반복됨

c.insert(2, 999)
print(c)

d = ['a', 'b', 'c', 'd', 'e', ['f', 'g', 'h'], 'i', 'j']
print(d)
print(len(d))

print(d[5][1])

