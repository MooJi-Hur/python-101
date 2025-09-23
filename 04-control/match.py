# match ~ case # python 3.10 이후부터 나옴

a = input("1 ~ 3 사이에 있는 정수를 입력해주세요.")
# fallthrough 없음
# match 변수에 해당하는 값으로 바로 이동
# 순차적으로 조건을 검사하지 않아 메모리를 절약
match a :
    case "1" :
        print("one")
    case "2" :
        print("two")
    case "3" :
        print("three")

season = input("월 입력 : ")
match int(season):
    case 12 | 1 | 2 :
        print("겨울")
    case 3 | 4 | 5 :
        print("봄")
    case 6 | 7 | 8 :
        print("여름")
    case 9 | 10 | 11 :
        print("가을")
    case _ :    # _: 특별히 값을 사용하고 싶지 않은데 변수가 필요할 때, default 키워드가 없음
        print("유효한 값을 입력하세요.")



