class MyIter:

    def __init__(self, end):
        self.end = end

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < self.end:
            self.current += 1
            return self.current
        else:
            raise StopIteration

    def __getitem__(self,index):     # Called to implement evaluation of self[key]
        if 0 <= index < self.end:
            return index + 1
        else:
            raise IndexError("Index out of range")

if __name__ == '__main__':
    for i in MyIter(10):
        print(i)

    print(list(MyIter(5)))

    # __getitem__을 대괄호를 가져오는 것으로 구현해둠
    print(MyIter(5).__getitem__(2))
    print(MyIter(5)[1])
