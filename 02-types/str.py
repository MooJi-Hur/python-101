# str : text sequence , 순서가 있음

# 큰 따옴표, 작은 따옴표는 혼용이 가능함
# single * 1
a = 'hello, world'
print(a)
print(type(a))

# double * 1
e = "hello, world"
print(e)

# escape sequence
# https://docs.python.org/3/reference/lexical_analysis.html#literals
# b = 'hello, 'world''
# '는 string의 시작 및 종료를 의미
# 일반적인 문자로 바꾸고 싶으면 역슬래시를 붙이면 됨
b = 'hello, \'world\''
print(b)

# single * 3 # 캐리지 리턴과 공백을 그대로 반영
c = '''hello
    python
        def'''
print(c)

# double * 3
d = """hello
    python
        def"""
print(d)

# 혼합
g = "hello, 'python'"
print(g)
h = 'hello, "python"'
print(h)

# str()
i = str("hello, world")
print(i)

# escape sequence
print("hello, \nworld")

# raw string
j = "c:\test"
print(j)
k = r"c:\test"
print(k)

# str + str
print("hello" + " " + "world" + "!!")
# print("hello" - "o")
print("hello" * 2)

# print("hello" + 1)  +는 동일한 타입의 연산자끼리 가능
print("hello" + str(1)) # 생성자로 해결

