# 소속 폴더가 파이선 패키지 코드로 구성되어 있다는 점을 알려줌, 패키지로 인식하게 만드는 폴더
# 기본 정보를 작성하는 용도
VERSION = "1.0.0"

# 초기화 시 미리 생성되어야 하는 것들 (database connection 등 설정)
def print_version():
    print(VERSION)

print_version()


# import *을 작성했을 시 사용할 수 있는 파일을 정의
__all__ = ["mytest"]