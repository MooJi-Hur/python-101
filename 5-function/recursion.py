# 3! = 3*2*1

def factorial_loop(n):
    current = 1
    for i in range(n, 0, -1):
        current *= i

    return current


def factorial_recursion(n):
    # 기저 조건
    if n == 1:
        return 1

    return n * factorial_recursion(n - 1)

    # 5! = 5 * factorial_recursion(4)

    # 실행된 코드
    # fact(5) -> 5 * fact(4) -> 4 * fact(3) -> 3 * fact(2) -> 2 * fact(1) -> 1

    # 누적된 결과는 역순으로 나옴
    # 1 -> 2 * 1 -> 3 * 2 * 1 -> 4 * 3 * 2* 1 -> 5 * 4 * 3 * 2 * 1

if __name__ == "__main__":
    print(factorial_loop(5))
    print(factorial_recursion(5))

