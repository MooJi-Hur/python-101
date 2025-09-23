msg = input("추가할 내용 : ")

file = open("test01.txt", "a", encoding="utf-8")

file.write(msg + "\n")

file.close()