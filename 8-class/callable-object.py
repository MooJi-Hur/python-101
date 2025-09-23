class Hello:
    def __call__(self, name):   # 호출할 수 있는 객체로 만들어줌
        # __init__과 달리 객체를 생성할 때가 아니라 사용할 때 호출하여 인자를 전달할 수 있음

        print(f"Hello, {name}")


if __name__ == '__main__':
    # greeting에는 인스턴스 주소가 들어가 있음
    greeting = Hello()

    # 객체에 괄호를 더 붙임 callable object, 객체를 함수처럼 사용할 수 있음
    greeting("MooJi!")

