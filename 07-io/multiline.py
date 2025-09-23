messages = ["There\n", "are\n", "lots\n","of\n", "lines\n"]

file = open("test01.txt", "a", encoding="utf-8")

file.writelines(messages)

file.close()