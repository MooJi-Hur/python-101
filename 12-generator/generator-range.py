def my_range(start = 0, stop = 0, step = 1):

    while start < stop:
        yield start
        start += step



if __name__ == '__main__':
    print(my_range(stop=10))
    print(list(my_range(1, 10)))

    for i in my_range(1, 11, 2):
        print(i, end=" ")