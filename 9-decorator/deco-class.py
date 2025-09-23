# 클래스로 데코레이터 만들어보기

class Greeting:

    def __init__(self, func):
        self.func = func

    # callable object : 객체를 함수처럼 호출
    # 데코레이터로 쓰기 위해 꼭 필요함
    # 클래스를 함수로 호출해서 사용하기 위해서는 생성 및 호출 기능이 필요하여 __init__과 __call__이 필요
    def __call__(self, *args, **kwargs):
        print("Hello,", end=" ")
        # __init__에서 self.func를 선언했기 때문에, 인스턴스 변수로 사용할 수 있음
        self.func(*args, **kwargs)


@Greeting
def my_func():
    print("World!")

if __name__ == "__main__":
    my_func()
    # Greeting(my_func) -> instanate -> __init__ 호출, 인스턴스가 됨
    # Greeting(my_func)을 다시 호출하면 __call__이 실행됨
    # Greeting(my_func)()


# class내 __call__이 클로저 함수로 구현된 경우, 함수를 인자로 전달했음
class Greeting:

    def __init__(self, name):
        self.name = name

    def __call__(self, func):

        def wrapper(*args, **kwargs):
            print(f"Hello, {self.name}")
            func(*args, **kwargs)

        return wrapper

@Greeting("python")
def my_func():
    print("Hello, World!")

if __name__ == "__main__":
    my_func()
    # Greeting("python")(my_func)()
