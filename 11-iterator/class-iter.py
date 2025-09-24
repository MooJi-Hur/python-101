class MyIter:

    def __init__(self, end):
        self.start = 0
        self.end = end
        self.value = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start <= self.end:
            self.value = self.start
            return self.value
        else:
            raise StopIteration

    def __getitem__(self,index):     # Called to implement evaluation of self[key]
        if self.start <= self.end:
            return list(self)[index]
        else:
            return IndexError

if __name__ == '__main__':
    for i in MyIter(10):
        print(i)

    print(list(MyIter(5)))

    # __getitem__을 대괄호를 가져오는 것으로 구현해둠
    print(MyIter(5).__getitem__(2))
    print(MyIter(5)[1])
