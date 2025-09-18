# closure : 맥락을 가진 함수, 함수와 함수가 선언된 환경을 함께 저장
# 닫힘이라는 뜻, 외부 함수에 있는 변수를 함께 기억
# 외부 함수의 역할 : 클로저 함수를 정의, 클로저 함수에 필요한 다른 변수 등 환경 기재, 내부 함수를 리턴
#

def greetings_not_closure(name):
    prefix = f"Hello, {name}!"

    # lexical scope : suffix라는 함수가 선언될 때, 함수의 범위가 정해짐
    # suffix가 return되면 greetings도 종료되지만,suffix를 실행 시 greetings의 환경(prefix, name)도 함께 넘어감

    def suffix():
        return prefix + name + "님 환영합니다."

    # 함수가 값으로 사용됨 일급 함수
    return suffix() # suffix와 suffix()는 다름  # 리턴 시점에 문자열 결과를 반환

def greeting_with_closure(name):
    prefix = f"Hello, {name}!"

    # lexical scope : suffix라는 함수가 선언될 때, 함수의 범위가 정해짐
    # suffix가 return되면 greetings도 종료되지만,suffix를 실행 시 greetings의 환경(prefix, name)도 함께 넘어감
    def suffix():
        return prefix + name + "님 환영합니다."

    # 함수가 값으로 사용됨 일급 함수
    return suffix

if __name__ == "__main__":
    message = greetings_not_closure("John") # greetings("John")인 경우도 다름 suffix(), gre..()()는 함수 호출 실점이 다름
    print(message)

    message = greeting_with_closure("John")() # 함수를 호출하고, 호출 시점에 문자열 결과를 반환
    print(message)


