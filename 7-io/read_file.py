file = open("test01.txt", "r")

# 읽으면서 줄을 소모함
# read_txt = file.read()
# print(read_txt)
#
# readline_txt = file.readline()
# print(readline_txt)

readlines_txt = file.readlines()    # 줄 단위 요소로 리스트로 반환
print(readlines_txt)

file.close()