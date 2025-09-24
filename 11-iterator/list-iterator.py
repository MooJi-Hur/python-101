# Iterable : 순서대로 값을 꺼내올 수 있다는 특징
# Iterator : 순서대로 값을 꺼낼 수 있는 객체
# lazy evaluation : 미뤘다가 실행될 때 연산됨
# __iter__() : iterator 반환

nums = list(range(20, 31))
print(nums)
print(dir(nums))

nums_iter = nums.__iter__()
print(nums_iter)    # <list_iterator object at 0x10aaae3b0>
print(dir(nums_iter))
print(type(nums_iter))  # <class 'list_iterator'>

print(id(nums))
print(id(nums_iter))

print(nums_iter.__next__()) # 처음 실행하면 index 0에 해당하는 값을 가져옴 # 20
print(nums_iter.__next__()) # 21
print(nums_iter.__next__()) # 22

# 아래 구문을 사용하고 나면 nums_iter를 모두 소진함
# print(list(nums_iter))  # [23, 24, 25, 26, 27, 28, 29, 30]

for item in nums_iter:
    print(item)


