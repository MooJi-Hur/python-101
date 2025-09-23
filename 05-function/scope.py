# 전역 변수
x = 10

def print_global():
    print(x)

print_global()


def print_local():
    # 지역 변수
    x = 20  # 전역 변수 x는 여전히 10
    print(x)

print_local()
print(x)


def keyword_global():
    global x
    x = 30  # 전역 변수 x에 할당
    print(x)

keyword_global()
print(x)    # 30


def declare_global_in_function():
    global y    # 함수 내에서 선언한 전역 변수, 호출 이후 외부에서도 y 사용 가능
    y = 3
    print(y)

declare_global_in_function()
print(y)

# shadowing : 3개의 y는 모두 다른 y
# 같은 변수 이름으로 지역마다 다르게 사용

def outer_no_global():
    y = 6

    def inner():
        y = 9
        print(f"inner y : {y}") # 9 중첩된 내부 함수의 변수 y

    inner()
    print(f"outer y : {y}") # 6 중첩된 외부 함수의 변수 y

outer_no_global()
print(f"global y : {y}")    # 3 기존에 선언했던 전역 변수 y

def outer_with_global():
    global y
    y = 6   # 전역 변수를 변경

    def inner():
        y = 9
        print(f"inner y : {y}")

    inner()
    print(f"outer y : {y}")

outer_with_global()
print(f"global y : {y}")


def outer_with_nonlocal():
    y = 9

    def inner():
        nonlocal y  # 지역 변수로 사용하는 것이 아니다라는 의미, 상위 함수 내 변수를 변경
        y = 3   # outer 함수의 y를 변경
        print(f"inner y : {y}")

    inner()
    print(f"outer y : {y}")

outer_with_nonlocal()
print(f"global y : {y}")

# 호출 순서 그림 이해 완료



