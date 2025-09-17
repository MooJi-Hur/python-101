# 입력한 값의 타입 확인, 2를 입력하면 str을 반환
# a = input()
# print(a)
# print(type(a))


# name = input("What is your name?")
# print(f"Hello, {name}!")

# 이름, 국어, 수학, 영어 점수를 입력받아서 dictionary로 만들기
# key는 각각 name, kor, math, eng
# sum, average로 합과 평균을 저장하고 딕셔너리를 출력하기

name = input("What is your name?")
kor = input("What is your korean?")
math = input("What is your math?")
eng = input("What is your english?")

total = int(kor) + int(math) + int(eng)
average = total / 3

myInfo = {
    "name" : name, "kor" :kor, "math" :math,
    "english" :  eng, "sum" : total, "average":  average
}

myItems = myInfo.items()
print(myItems)