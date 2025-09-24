def my_generator(end):
    i = 0
    while i < end:
        i += 1

        yield i ** 2    # __next__() 호출을 기다림    # generator

if __name__ == '__main__':
    nums = my_generator(10)
    print(nums)
    print(type(nums))

    # 함수에 대한 콜스택은 함수마다 별개로 있음
    print(nums.__next__())
    print(nums.__next__())

# 원하는 값을 상황에 따라 하나씩 만들고 싶을 때 generator를 사용
def subject_generator():
    yield "python"
    yield "java"
    yield "cpp"


if __name__ == '__main__':
    subjects = subject_generator()

    print(subjects)
    print(dir(subjects))    # __iter__, __next__가 있음
    print(type(subjects))

    print(subjects.__next__())
    print(subjects.__next__())
    print(subjects.__next__())
    print(subjects.__next__())  # stop iteration