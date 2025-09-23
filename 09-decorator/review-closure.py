def outer():
    prefix = "outer"

    def inner():
        print(f"{prefix}, inner")

    # closure : lexical environment
    # outer 내부를 lexical scope라고 부름
    return inner



# 함수가 값으로 들어옴, 일급 함수 - 함수 자체를 값으로 사용하고 있음
# 호출 2 파라미터에 outer 저장
def func_param(func):
    # 호출 3  outer 호출
    # 호출 4  return 되면서 inner 호출
    func()()


if __name__ == "__main__":
    # 호출 1 func_param 실행
    func_param(outer)

