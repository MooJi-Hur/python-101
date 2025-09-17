# 산술 연산
# dir(int)에서 operander 구현 상태를 확인할 수 있음
a = 17
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

# 거듭제곱 power
print(a ** b)

# 몫 floor division : 소숫점 이하는 버림
print(a // b)

# 나머지 modulo
print(a % b)

# 비교 연산
a, b = 5, 3
print(a == b)
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)

# print(a =< b)   SyntaxError

print(a is b)
print(a is not b)

# 여러 값을 한 번에 비교하기
print(1 < b < a)


# 기본적인 논리 회로 세 가지
# and : 둘 다 True일 때 참
print(a and b)
print(a & b)

print(True and True)
print(True & True)

# or : 둘 중 하나만 True여도 참
print(True or False)
print(True | False)

# not -> !는 동작하지 않음
print(not True)
print(not False)


# 멤버 연산
list01 = [1, 2, 3, 4, 5]

# True 혹은 False 반환
print(3 in list01)
print(6 in list01)
print(3 not in list01)

# range : 해당 범위의 숫자 생성 # python 내장 함수 -> 문서 확인
# range(0, 10) 반환, 메모리에 시작점과 종료점을 따로 담아둠, 공간 절약
# iterable 객체 반환
print(range(10))

# range(stop) : 0 ~ stop -> stop - 1 까지의 값을 만드는 것을 확인 가능
# 0부터 시작하여 정수 갯수
print(list(range(10)))

# range(start, stop) : start ~ stop - 1
list02 = list(range(10, 20))
print(list02)

# range(start, stop, step) : start, start + step, ..., stop - 1
# 끝 점을 포함하지 않음
print(list(range(1, 11, 2)))
print(list(range(10, 0, -1)))

# slice
original = list(range(100))
print(original)

# [n] : n index
print(original[5])  # 5

# [start:stop]
slice01 = original[1:5]
print(slice01)   # start ~ stop - 1

# [start:stop:step]
slice02 = original[10:20:2] # start, start + 2, ... stop - 1
print(slice02)


# 숫자를 넣지 않는 경우
print(original[:50]) # 0 ~ 50 - 1 # start default = 0
print(original[50:]) # 50 ~ 99 # stop default = len - 1
print(original[::10]) # start stop 모두 default

# 거꾸로
slice03 = original[20:10:-1]    # 10을 포함하지 않음 확인
print(slice03)


# 문자열
welcomeMessage = "Hello, World!"
print(len(welcomeMessage))
print(welcomeMessage[:len(welcomeMessage)-1])   # len(welcomeMessage)-1 = 12
print(welcomeMessage[-1:])
print(welcomeMessage[:-1])

# -1
print(welcomeMessage[-1])   # startIndex를 -로 함
print(welcomeMessage[:-1])  # stopIndex - 1
print(welcomeMessage[::-1])  # 역순

welcomeMessage = "Hello, World!"
print(welcomeMessage[7:-1])


# 증감 연산자
c = 10
# c라는 변수에 저장된 값에 1을 더한 뒤 다시 c에 저장하고 싶어

c = c + 1
print(c)

c += 1  # syntax sugar
print(c)


c -= 1
print(c)

c *= 2
print(c)
c /= 2  # 실수인 결과를 반환
print(c)
c %= 2
print(c)










