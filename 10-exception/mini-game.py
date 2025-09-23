from random import randint


'''
가위바위보 게임
출력 예)

가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 1
player (가위) vs computer(보) : 당신이 이겼습니다.
가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 2
player (바위) vs computer(가위) : 당신이 이겼습니다.
가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 3
player (보) vs computer(가위) : 컴퓨터가 이겼습니다.
가위 : 1 | 바위 : 2 | 보 : 3 | 게임종료 : 4 -> 숫자를 입력하세요 : 4
다음에 또 놀러오세요
'''

class RockScissorPaperException(Exception):
    def __init__(self):
        print("1, 2, 3, 4 중 하나의 값을 입력하세요.")

# 가위바위보 만들기
def game_process(player_num: int) -> None:
    pass


def play() -> None:
    while True:
        try:
            player_num = int(input("가위 : 1 | 바위 : 2 | 보 : 3 | 게임 종료 4 -> 숫자를 입력하세요. "))

            if player_num not in [1, 2, 3, 4]:
                raise RockScissorPaperException()
            if player_num == 4:
                break
        except ValueError as e:
            print(e)
            print("숫자만 입력하실 수 있습니다. \n다시 입력해주세요.")

        except RockScissorPaperException as e:
            print(e)
            print("\n다시 입력해주세요.")
        except Exception as e:
            print(e)
            break
        else:
            game_process(player_num)

        print("다음에 또 놀러오세요.")



if __name__ == '__main__':
    play()
