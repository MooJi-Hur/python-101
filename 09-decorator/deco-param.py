
def greeting(func):
    def print_out():
        print("Hello, ", end="")
        func()

    return print_out

@greeting   # 클로저 함수를 선언하면 데코레이터로 사용 가능
def myfunc():
    print("World!")

if __name__ == "__main__":
    # greeting(myfunc())()
    myfunc()


# 파라미터가 있는 경우
def greeting(func):

    def print_out(name):
        print("Hello, ", end="")
        func(name)

    return print_out    # print_out 함수 자체를 값으로 반환하고 있음


@greeting
def myfunc(name):
    print(name)

if __name__ == "__main__":
    # greeting(myfunc)("python!")
    myfunc("python!")

def greeting(func):

    def print_out(*args, **kwargs):
        print("Hello, ", end="")
        func(*args, **kwargs)

    return print_out

@greeting
def param_func(name):
    print(name)

@greeting
def no_param_func():
    print("python!")

if __name__ == "__main__":
    param_func("MooJi")
    no_param_func()


# 호출 3 -> World 전달 , lexical scope의 사용 례, 파라미터로 지역변수이면서 동시에 렉시컬 스코프 활용
def greeting(name):

    # 호출 4
    def wrapper(func):

        def print_out():
            print(f"Hello, {name}!")
            func()

        return print_out

    return wrapper


# 호출 2
@greeting("World")
def yes_deco_my_func():
    print("Hello, Python!")


if __name__ == "__main__":
    # 호출 1
    yes_deco_my_func()

def no_deco_my_func():
    print("Hello, Python!")


if __name__ == "__main__":
    # greeting에 대한 인자 위치 확인
    # greeting("World") -> wrapper
    # wrapper(no_deco_my_func) -> wrapper(no_deco_my_func) -> print_out
    # print_out()
    greeting("World")(no_deco_my_func)()


from datetime import datetime
from time import sleep


# 같은 데코레이션을 여러 함수에 사용하는 경우
def my_logger(name):
    def wrapper(func):
        def logging():
            print(f"{name}: {datetime.now()}")
            func()
            print(f"{name}: {datetime.now()}")

        return logging
    return wrapper

@my_logger("mooji")
def greeting():
    sleep(2)
    print("Hello, World!")


@my_logger("hong-gd")
def goodbye():
    sleep(2)
    print("Good bye, World!")

if __name__ == "__main__":
    greeting()
    print("---")
    goodbye()