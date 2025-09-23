from abc import ABC,ABCMeta, abstractmethod

# 객체 지향 프로그램 특징 : 추상화
# 공통적인 개념을 묶음
# https://docs.python.org/3/reference/datamodel.html#metaclasses

# 추상 클래스를 만드는 두 가지 방법 metaclass

# ABC : Abstract Base Class
class AbstractParent(ABC):
    def print_out(self):
        print("abstract class : 추상 함수를 가질 수 있는 클래스")

    # 내용은 알아서 하되, 반드시 구현해야할 함수를 정의
    @abstractmethod
    def abstract_method(self):
        pass

class FirstChild(AbstractParent):
    def abstract_method(self):
        print("abstract method : 상속받은 자식 클래스에서 반드시 구현")

if __name__ == '__main__':
    # 추상 클래스로는 객체를 생성할 수 없음
    # abstract_parent = AbstractParent() # 정의만 되어있고, 구현되어 있지 않아
    # 객체 생성을 할 수 없게 해둠, 자식이 생성을 받아서 구현을 해야만 함
    # 자식이 반드시 필요
    # TypeError: Can't instantiate abstract class AbstractParent
    # without an implementation for abstract method 'abstract_method'

    child = FirstChild()
    child.print_out()
    child.abstract_method()


# metaclass : class를 만들어주는 class
class AbstractParent(metaclass=ABCMeta):
    def print_out(self):
        print("추상 클래스")

    @abstractmethod # 자식 클래스에서 반드시 구현해야하는 메소드
    def abstract_method(self):
        pass

class SecondChild(AbstractParent):    # 인자료 부모 클래스를 넣어줌
    def abstract_method(self):
        print("추상 매서드")

if __name__ == '__main__':
    child = SecondChild()
    child.print_out()   # 부모에서 정의한 함수를 사용할 수 있음
    child.abstract_method()


class Character(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):   # 언젠가는 자식 클래스가 해당 함수를 구현해야함
        pass

class Knight(Character):
    def attack(self):
        print(f"{self.name} : 칼로 공격")

class Archer(Character):
    def attack(self):
        print(f"{self.name} : 활로 공격")


if __name__ == '__main__':
    charactor = None    # 변수 선언

    select = int(input("1 : 기사 \n2 : 궁수\n 직업을 선택해주세요. \n"))

    match select:
        case 1:
            charactor = Knight("기사")     # 인스턴스 객체를 참조한는 변수가 됨

        case 2:
            charactor = Archer("궁수")

    charactor.attack()

# 다형성 polymorphism
