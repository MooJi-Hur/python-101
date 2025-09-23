class A:
    pass

class CreateMeta(type):
    def __new__(cls, *args, **kwargs):
        print("metaclass new")
        return super().__new__(cls, *args, **kwargs)

    def __init__(cls, *args, **kwargs):
        print("metaclass init")

    def __call__(cls, *args, **kwargs):
        # callable object로 만들어줌
        print("metaclass call")
        return super().__call__()


if __name__ == "__main__":
    num = 10
    '''
        class type(object):
        """
        type(object) -> the object's type # 메타 클래스, 새로운 클래스를 만드는 클래스
        By default, classes are constructed using type().
        type(name, bases, dict, **kwds) -> a new type   
        """
    '''
    print(type(num))
    # 변수는 값이 저장된 메모리의 주소값
    # 값은 인스턴스를 의미, 파이썬은 모든 것이 객체
    # A 클래스의 값의 형태는 type, A라는 클래스의 인스턴스의 type이 type
    # class는 값이면서, 객체
    print(type(A)) # <class 'type'>


    # type을 이용해서 클래스를 생성
    # type은 class를 생성하는 metaclass
    # base 타입을 별도로 전달하지는 않음 ()

    # hello_type = Hello World라는 클래스
    # <class '__main__.Hello, World!'>
    # 새로운 타입을 생성
    hello_type = type("HelloWorld", (), {})
    print(hello_type)

    # 새로 만든 타입의 인스턴스를 생성
    # 인스턴스의 위치
    # <__main__.Hello, World! object at 0x1061a0050>
    hello = hello_type()
    print(hello)


    # MyClass라는 클래스를 생성
    """
    metaclass new
    metaclass init
    <class '__main__.MyClass'>
    """
    metaclass = CreateMeta("MyClass", (), {})
    print(metaclass)
    # <class '__main__.MyClass'>
    # metaclass call
    myInstance = metaclass()
    print(myInstance)




