# type annotation types
# type hint

# 함수의 return 값이 있는 경우, 해당 값의 type을 미리 작성해두는 것

def sum_type_hint(a, b) -> int: # 강제성 없음
    x, y = int(a), int(b)

    return x + y


# parameter의 type
def connect_parameter(a: int, b: str) -> str:
    connect = str(a) + b

    return connect

# parameter : type = default

def param_hint_default(a : int=0, b: int=0) -> int:
    return a + b

if __name__ == '__main__':
    c: int = 1  # 변수의 타입을 설명
    print(sum_type_hint(c, 2))
    print(connect_parameter(1, "2"))
    print(param_hint_default(1))

    # pep484