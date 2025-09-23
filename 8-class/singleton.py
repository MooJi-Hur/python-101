class mySingleton(type):
    # instance 주소 저장
    __instance = {}  ## dict
    print(__instance)

    # __call__ : class를 함수처럼 호출할 수 있도록 만듦
    # callable object
    def __call__(self, *args, **kwargs):

        if self not in self.__instance:
            self.__instance[self] = super().__call__(*args, **kwargs)   # super().__call__의 리턴 값이 주소값
        print(self.__instance) # {<class '__main__.MyClass'>: <__main__.MyClass object at 0x10ea94050>}
        return self.__instance[self]    # 출력 결과가 주소값이 됨

class MyClass(metaclass=mySingleton):
    pass

if __name__ == "__main__":
    myInstance = MyClass()
    yourInstance = MyClass()

    # 동일한 메모리에 인스턴스를 생성한 주소를 확인
    # numeric은 singleton으로 값이 저장됨
    # 메모리에 객체를 하나로만 저장할 때 사용
    print(myInstance)
    print(yourInstance)

    print(myInstance == yourInstance)