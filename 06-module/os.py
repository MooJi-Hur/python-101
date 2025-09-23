import os

print(os.environ)

print(os.environ.keys())


# 환경 변수 조회
print(os.environ.get("PWD"))
print(os.environ.get("HOME"))
print(os.environ.get("USER"))

print(os.getcwd())

print(os.listdir())

if not os.path.exists('./test'):
    os.mkdir('./test')

os.rename("./test", "./renamed")