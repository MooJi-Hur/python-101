# 예외 처리 : 에러가 발생했을 대, 프로그램이 비정상적으로 종료되는 것을 방지하기 위함


try:
    # 예외가 발생할 가능성이 있는 코드
    pass
except:
    # 예외 발생 시 수행할 코드
    pass
else:
    # 정상 수행 되었을 때 수행할 코드
    pass
finally:
    # 에러 발생 여부와 관계없이 실행할 코드
    pass


def error_mod():
    print(10 / 0)

def exception_mod():
    try:
        print(10 / 0)
    except:
        print("0으로 나눌 수 없습니다. ")

def exception_mod_case():
    try:
        print(10 / 0)
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다. ")


def exception_multi_case():
    try:
        a = [1, 2, 3, 4, 5]
        print(a[5])
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다. ")
    except IndexError:
        print("index를 확인해 주세요. ")

def exception_multi_case_alias():
    try:
        a = [1, 2, 3, 4, 5]
        print(a[5])
    except ZeroDivisionError as e:
        print(e)
    except IndexError as e:
        print(e)

def exception_common():
    try:
        a = [1, 2, 3, 4, 5]
        print(a[5])
    except Exception as e:  # 무슨 에러일지 모를 때, 모두 잡는 용도, 가장 아래에 두어야 다른 예외를 잡음
        print(e)

def exception_else():
    try:
        a = [1, 2, 3, 4, 5]
        print(a[5])
    except Exception as e:
        print(e)
    else:
        print("에러 없음")
    finally:
        print("항상 실행")

def else_case():
    try:
        a = [1, 2, 3, 4, 5]
        print(a[4])
    except Exception as e:
        print(e)
    else:
        print("에러 없음")
    finally:
        print("항상 실행")  # 열었던 객체를 닫는 용도로 많이 사용


def input_num():
    while True:
        try:
            n = int(input("숫자를 입력해주세요: "))  # 이 지역 변수를 함수 내에서 사용할 수 있음
            break
        except ValueError:
            print("입력한 값이 숫자가 아닙니다. 다시 입력해주세요.")  # while문 활용, 재입력 가능

    return n

if __name__ == '__main__':
    # error_mod()  # division by zero
    exception_mod()
    exception_mod_case()
    exception_multi_case()
    exception_multi_case_alias()
    exception_common()
    exception_else()
    else_case()
    a = input_num()
    b = input_num()
    print(f"{a} + {b} = {a + b}")