# parameter : 함수 외부에서 전달되는 값을 받아서 함수 내부에서 사용하기 위한 변수

def sum2(x):    # x는 parameter
    return x + 2

# argument : 함수 외부에서 전달되는 값
print(sum2(5))  # argument 5

def sum_x_y(x, y):
    result = x + y
    return result

print(sum_x_y(2, 3))    # 값을 직접 지정하지 않으면 순서대로 들어감
print(sum_x_y(x=10, y=20))
print(sum_x_y(y=30, x=20))    # 아규먼트와 맵핑되는 파라미터를 명시하면 순서를 바꿔도 됨

# 실행되는 곳의 이름 __name__ 현재 파일이면 main
# 직접 실행되면 이름이 "__main__", 코드 파일 외의 다른 파일에서 호출하면 자신의 파일 이름이 됨
print(f"__name__ : {__name__}")

if __name__ == "__main__":  # 파일의 시작점
    print(sum2(100))
    print(sum_x_y(1000, 2000))


def get_param(param):
    print(f"parameter 내 저장되어 있는 값 : {param}")

def get_param_default(a, b="default"):
    print(a)
    print(b)

# *args : arguments -> 여러 개의 값을 받을 수 있음 - packing
# 받아야하는 값의 갯수를 정하지 않고 묶어서 처리할 수 있음
def param_arguments(*args): # *을 붙이는 것이 중요, args라고 직접 안써도 됨
    print(args)
    for i , arg in enumerate(args):
        print(f"{i} : {arg}")

# **kwargs : keyword arguments -> key, value 형태로 받을 것이라는 의미
def param_kwargs(**kwargs):
    print(kwargs)   # dictionary로 받아줌
    for k, v in kwargs.items():
        print(f"key : {k} \t value : {v}")

def param_args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__=="__main__":
    get_param("arguments")
    get_param_default(1, 2)
    get_param_default("abc")
    get_param_default(a="def") # default가 없으면, 파라미터를 입력하지 않을 때 타입 에러
    get_param_default("aa", b="bb")

    param_arguments("a", "b")
    param_arguments(1, 2, 3)
    param_arguments(["a", "b", "c"])    # 리스트 통째로 하나의 아규먼츠
    param_arguments(*["a", "b", "c"])   # 리스트 내의 원소를 각각의 아규먼츠로 넣음

    param_kwargs(a=1, b=2, c=3) # key=value 형태로 아규먼츠 입력

    # 딕셔너리를 통째로 넣으면 key갈
    # param_kwargs({"a": 4, "b": 5, "c": 6})  # TypeError: param_kwargs() takes 0 positional arguments but 1 was given
    # param_kwargs(*{"a": 4, "b": 5, "c": 6})     # TypeError: param_kwargs() takes 0 positional arguments but 3 were given
    param_kwargs(**{"a": 4, "b": 5, "c": 6})    # 정상 실행

    param_args_kwargs("a", "b", "c", e=5, f=6, g=7)  # 아규먼트 형태 확인



