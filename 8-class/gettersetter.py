class HelloGetterSetter:
    def __init__(self, name="mooji"):
        self.name = name

        # 변수명 앞에 __를 사용하면 private
        self.__age = 100

    # @ ~ : decorator : 기능 추가

    # getter
    @property
    def age(self):
        return self.__age

    # setter
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"{self.name} 님은 {self.__age}세 입니다. "

if __name__ == '__main__':
    myInfoClass = HelloGetterSetter("MooJi Hur")
    print(myInfoClass)

    myInfoClass.age = 101
    print(myInfoClass)
    print(myInfoClass.age)