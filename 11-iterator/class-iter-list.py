class MyIter:
    def __init__(self, start=0, end = 0):
        self.start = start
        self.end = end

    def __iter__(self):
        for i in range(self.start, self.end + 1):
            yield i

    def __getitem__(self, index):
        if 0 <= index < len(self):
            return self.start +  index
        else:
            raise IndexError("Index out of range")

    def __len__(self):
        if self.end >= self.start:
            return self.end - self.start + 1
        else:
            return 0

if __name__ == "__main__":
    it = MyIter(10, 15)

    print(list(it))

    for x in it:
        print(x)

    print(it[3])
    print(len(it))