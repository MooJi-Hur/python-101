
# 함수를 값으로

# 호출 2
def greeting(func):
    def print_hello():
        print("Hello, ", end="")
        # 호출 3
        func()
    return print_hello


# 호출 4
def my_func():
    print("World!")

if __name__ == '__main__':
    # 호출 1
    greeting(my_func)() # -> 데코레이터로도 표기할 수 있음 Syntax sugar
    # decorator로 만들면 greeting이라는 함수에 myfunc가 값으로 전달됨
