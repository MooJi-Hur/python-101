from random import randint

# 1 ~ 45 까지의 중복되지 않는 랜덤한 숫자 6개를 정렬하여 리턴하자
def make() -> set:
    candidate = set()
    while(len(candidate)<=5) :
        candidate.add(randint(1, 45))

    return sorted(candidate)


if __name__ == '__main__':
    print(make())
