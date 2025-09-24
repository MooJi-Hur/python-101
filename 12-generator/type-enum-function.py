from enum import Enum

Color = Enum('Color', ('RED', 'BLUE', 'GREEN'))

# enum : 상수 저장
# enum을 사용하는 이유

if __name__ == '__main__':
    print(Color)    # generator object .. 필요할 때 값을 만들어 줄거야
    print(Color.RED)
    print(Color.RED.name)
    print(Color.RED.value)

    print(Color.__iter__())
    print(list(Color.__iter__()))