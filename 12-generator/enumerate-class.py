class MyEnumerate:

    @staticmethod
    def my_enumerate(iterable_object):
        index = 0
        for item in iterable_object:
            yield index, item
            index += 1

if __name__ == '__main__':
    subjects = MyEnumerate().my_enumerate(["python", "numpy", "pandas"])
    print(dict(subjects)) # 이전 코드에서 iterator를 소비해버렸는지 확인할 것
    print(list(subjects))   # 포인터를 소진했으므로 빈 리스트를 출력
