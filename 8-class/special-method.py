# special method (magic method)


"""
연산자
__ge__() : >=
__gt__() : >
__le__() : <=
__lt__() : <
__eq__() : ==
__ne__() : !=
...
__and__() : &
__or__() : |
...
__add()__ : +
__sub()__ : -

...
__str__() : 사람이 읽을 수 있는 방식으로 객체의 표현 값을 반환
__repr__() : 다른 객체를 위해 객체 표현 값 반환
# print()는 __str__을 먼저 호출, __str__이 없으면 해당 되는 값이 없으면 __repr__ 호출
# repr : official string representation
# __repr__로 리턴되는 값은 eval()의 arg로 값을 넣었을 때 객체가 생성되는 표현 값을 리턴하도록 권장
"""

class Line:
    def __init__(self, length = 0):
        self.length = length
        print(f"선 길이 : {length}")


    # 재정의 overriding 아래부터는 객체를 비교
    def __eq__(self, other):
        return self.length == other.length

    def __ne__(self, other):
            return self.length != other.length

    def __str__(self):
        return f"선 길이 : {self.length}"  # return 값이 스트링

    def __repr__(self):
        # 반환 값은 새 객체를 생성할 수 있는 내용으로 작성할 것을 권장함
        return f"Line(length={self.length})"    # return 값이 스트링

    # special method 연산자 사용 시 어떻게 동작할지 추가한 것, 정의하지 않으면 지원하지 않는 기능
    # 객체를 비교하는데 꼭 필요한 기능은 아님
    def __add__(self, other):
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __gt__(self, other):
        return self.length > other.length

    def __ge__(self, other):
        return self.length >= other.length

    def __lt__(self, other):
        return self.length < other.length

    def __le__(self, other):
        return self.length <= other.length



if __name__ == "__main__":
    lineTen = Line(10)
    lineThree = Line(3)

    print(f"lineTen: {lineTen.length}")
    print(f"lineThree: {lineThree.length}")

    print(f"lineTen + lineThree = {lineTen.length + lineThree.length}")
    print(f"lineThree - lineTen = {lineThree.length - lineTen.length}")
    print(f"lineThree - lineTen = {lineThree.length.__sub__(lineTen.length)}")

    print(lineTen)
    print(f"__str__ : {lineTen.__str__()}")
    print(f"__repr__ : {lineTen.__repr__()}")

    # eval : 실행
    print("eval : ")
    eval(f"{lineTen.__repr__()}")   # 명령이라 생각하고 스트링 내의 내용을 실행
    eval(f"print(Line(3) + Line(4))")