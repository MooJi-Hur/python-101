# lamda 표현식 : 익명 함수 표현식

# lambda param: expression

def sum10(x, y):
    return x + y + 10

print(sum10(1, 2))

# 변수에 담아서 사용하려면 굳이 lambda를 사용하지 말고 함수를 선언해라
# lambda는 함수를 '간단'하게 한 번만 호출 싶을 때 사용, 문법적 이유
sum20 = lambda x, y: x + y + 20 # 함수 이름이 없음 Syntax Sugar

print(sum20(1, 2))

# 간단하게 사용한 예시, (lambda 표현식)(아규먼츠)인 문법 확인
print((lambda x, y, z : x * y / z)(10, 20, 30))

tuple_list = [
    (1, "one", 9), (2, "two", 8),(4, "four", 6),
    (3, "three", 7),
]

print(tuple_list)

# 람다 표현식을 쓰는 예
tuple_list.sort(key=lambda x :x[1])   # sort(*, key=None, reverse=False)
print(tuple_list)

# 중첩도 가능, 잘 사용하지는 않음
result = (lambda x: lambda y: x + y)(10)(20)    # 10이 x에 전달됨, 20이 y에 전달됨
print(result)

nested = (lambda x: lambda y: x + y)(10)
print(nested)   # 함수 구현체의 주소가 나옴  lambda y : 10 + y가 바깥 함수의 명령어

nested_result = nested(20)
print(nested_result)


# 1 ~ 100 사이의 리스트
hundred = [i for i in range(1, 101)]

# 1 ~ 100 사이에서 5의 배수만 가지는 list # 5로 나눈 나머지가 0일 때 5의 배수
# bool 생성자 사용
five_times = [i for i in range(1, 101) if not (lambda x: bool(x % 5))(i)]
print(five_times)

# if문 이용
five_times = [i for i in range(1, 101) if not (lambda x: x if (x % 5) !=0 else None)(i)]

# zip
num = [1, 2, 3]
char = ["a", "b", "c"]
zipped = zip(num, char) # 두 리스트의 길이가 반드시 같아야 함
print(zipped)
print(list(zipped))

# map : 리스트 내 각각의 값에 함수를 실행하여 반환
map_result = map(lambda x: x * 10, num)
print(map_result)   # map 객체만 반환
print(list(map_result))

print(list(map(lambda x: x.upper(), char)))


# filter
print(filter(lambda x: x > 1, num))
print(list(filter(lambda x: x > 1, num)))   # 참인 결과만 담겨져 있음

# 숙제
# test_list에서 숫자만 새로운 list로 만들어서 출력하자
# str.isdigit(), list, filter, lambda
test_list = ["3", "6", None, "9", ""]



