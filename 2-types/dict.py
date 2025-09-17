# dictionary
# 순서 o, 중복 (key x, value o) #python3.6부터 순서가 존재

# {key : value, ...}
dict01 = {'a': 1, 'b': 2}
print(dict01)
print(type(dict01))

dict01['c'] = 3
print(dict01)

# dict()
dict02 = dict([('a', 1), ('b', 2)])
print(dict02)

dict03 = dict(a = 1, b = 2)
print(dict03)

dict04 = dict([['a', 1], ['b', 2]])
print(dict04)

print(dict03.keys())
print(dict03.values())
print(dict03.items())

# dict05 = dict02 + dict03 안됨
# print(dict05)

# dict 키 밸류 등 조회 값을 리스트로 변환
print(list(dict03.keys()))
print(list(dict03.values()))
