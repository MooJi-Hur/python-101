class HelloClass:

    def greetings(self):
        print("Hello, World!")

if __name__ == "__main__":
    myClass = HelloClass()
    myClass.greetings()

    # 클래스 이름과 주소 출력
    print(myClass)

    # 해당 클래스에서 만들어진 인스턴스인지 확인
    print(isinstance(myClass, HelloClass))

class HelloSelf:

    # 속성
    # class variable : 이 클래스의 모든 인스턴스가 사용가능
    suffix = "님 반갑습니다. "

    # special method (magic method)
    # 앞뒤로 __를 붙여 표기

    # __init__(self) __new__()를 호출하여 객체를 생성하고 초기화
    def __init__(self):
        # instance variable : 생성한 객체마다 다른 값을 가질 수 있음
        self.prefix = "안녕하세요."

    # 기능 : function(독립적) method(클래스에 종속적)

    def greetings(self, name):
        print(f"{self.prefix} {name}{HelloSelf.suffix}")

if __name__ == "__main__":
    myClass = HelloSelf()
    myClass.greetings("MooJi") # greetings는 인스턴스를 생성한 뒤에야 사용할 수 있음
    # HelloSelf.greetings("MooJi")는 동작하지 않음


    print(myClass)
    print(HelloSelf.suffix)
    print(myClass.prefix)
    print(myClass.suffix)

class HelloStr:
    def __init__(self, name="MooJi", age=100):
        self.name = name
        self.age = age

    # __str__ 객체의 주소값 리턴
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

if __name__ == "__main__":
    myStrClass = HelloStr("mooji", 32)
    print(myStrClass)
    print(myStrClass.__str__())
    print(myStrClass.__repr__())    # 객체의 주소값을 리턴하고 있음