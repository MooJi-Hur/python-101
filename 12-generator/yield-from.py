def generator_list(end):
    yield list(range(end))  # 키워드 뒤의 값 - 즉 리스트 자체를 리턴

def generator_from(end):
    # yield from 다른 제너레이터에 next를 전달하여 생성 값을 가지고 오게 해줌
    yield from list(range(end)) # 제너레이터에 yield를 다시 적용   # 값이 하나씩 출력

if __name__ == "__main__":
    list_generator = generator_list(10)
    for item in list_generator:
        print(item)

    print("---")

    from_list_generator = generator_from(10)
    for item in from_list_generator:
        print(item)