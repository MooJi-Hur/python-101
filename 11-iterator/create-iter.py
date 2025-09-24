# iterator를 만드는 두 가지 방식

# iter : builtin function
my_iter = iter([1, 2, 3, 4, 5])
# special method
your_list = [1, 2, 3, 4, 5]
your_iter = your_list.__iter__()

print(my_iter)
print(type(my_iter))

print(your_iter)
print(type(your_iter))

print(next(your_iter))
print(your_iter.__next__())

print('---')

for item in your_iter:
    print(item)

