class MyException(Exception):

    def __init__(self):
        super().__init__("myException")

def user_define_exception():
    try:
        a = 1
        b = 2
        if a + b == 3:
            # 예약어 raise 예외를 강제로 발생시킴
            raise MyException()
    except MyException as e:
        print(e)

if __name__ == '__main__':
    user_define_exception()