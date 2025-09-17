# f(x) : 함수 입력 -> 처리 -> 출력 : 기능

def print_hello():  # :은 함수 범위 시작
    print("hello, world!")
    print("hello, python!")

# 기능을 만든 뒤에는 호출을 해야 열림
print(print_hello())

def get_hello():
    msg = "hello, world!"
    return msg

get_hello()

print(get_hello())

def get_dict():
    return {"name": "admin", "message": "hello world!"}

print(get_dict()) # dict 객체 내용을 그대로 출력

result = get_dict()
print(f"name : {result["name"]}") # 함수 결과를 변수에 할당하여 다시 사용했음


def no_return():
    print("no return")
    return

print(no_return())  # 값이 없지만 return은 설정했음을 의미
                    # return 키워드를 사용하지 않아도 기본값이 None으로 일단 설정되어 있음

def test_multi_return():
    return 1    # 함수를 호출한 스레드에 값을 전달하고 종료, 메모리에서 사라짐
    return 2
    return 3

print(test_multi_return())   # 호출 시에 메모리에 할당됨
print(test_multi_return) # 함수 객체의 주소를 출력