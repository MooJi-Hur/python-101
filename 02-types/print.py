# print
# flush : stream에 남아있는 데이터를 강제로 출력

name = "mooji"
age = 22

print(name)
print(age)

# print(name + age) 불가능, 스트링끼리의 결합이 가능하며, 숫자는 str로 형변환을 해야 함
print(name + str(age))
# *args / **kwargs
print(name, age) # *object이므로 이런 형태가 가능
print(name, age, sep='-')
print(name, age, end='출력이 끝난 후 end가 출력 됩니다. ..')
print("??")

print("name", name, sep=":", end="\t")
print("age", age, sep=":")


# 기능이 나온 순서대로 살펴봄
# 타입을 기재하지 않아도 되고, 가독성이 좋아지는 방향으로 발전함
# % values
print("name: %s" % name)
print("name: %s \t age: %d" % (name, age))

# str.format()
print("name: {} \t age: {}".format(name, age))

# f-string
print(f"name: {name}\t age: {age}")
