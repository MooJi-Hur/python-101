class HelloPrivate:
    def __init__(self):
        self.public = "It's public."
        self.__private = "It's private."

    def __private_method(self):
        print(f"private method: {self.public}, {self.__private}")

    def public_method(self):
        print(f"public method: {self.public}, {self.__private}")

        # class 내부에서는 __private 함수 사용 가능
        self.__private_method()


if __name__ == '__main__':
    hello = HelloPrivate()
    print(hello.public)
    hello.public_method()
