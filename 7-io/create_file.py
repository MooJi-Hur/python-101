"""
r : 읽기
w : 덮어쓰기
a : 이어서 쓰기
x : 새로운 파일 만들어서 쓰기
t : text
b : binary
"""



file = open("test01.txt", "w")

file.write("hello, world! \n")

file.close()
