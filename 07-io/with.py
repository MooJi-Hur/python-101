with open("test01.txt", "r", encoding="utf-8") as file:
    # with는 close를 바로 사용하여 리소스를 관리
    for line in file.readlines():
        print(line)
