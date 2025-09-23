from dataclasses import dataclass
"""
order: If true (the default is False), 
__lt__(), __le__(), __gt__(), and __ge__() methods will be generated. 
"""
@dataclass(order=True) # 스페셜 메소드 설정
class Person:
    name: str
    age: int
    phone: str


@dataclass
class Address:
    addr: list[Person]

if __name__ == "__main__":
    hong = Person(name="Hong", age=82, phone="010-456-7890")
    lee = Person(name="Lee", age=32, phone="011-456-7890")
    kim = Person(name="Kim", age=42, phone="012-456-7890")

    # data class 데이터를 가지는 클래스
    # 출력 결과에서 객체의 주소가 아니라, 데이터를 바로 확인할 수 있음
    print(hong)
    print(lee)
    print(kim)

    print(f"{hong.name}님의 전화번호는 {hong.phone} 입니다. ")

    # order = True 로 인해 비교해도 에러가 출력되지 않음
    print(hong < lee)

    addr = Address([hong, lee, kim])
    print(addr)

