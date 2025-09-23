import pickle

"""
pickling (dump) : 객체를 파일에 바로 씀
unpickling (load) 파일을 객체로 로드
"""

score = {"name" : "hong", "kor": 100, "eng": 67, "math": 89}

with open("test02.txt", "wb") as file:
    pickle.dump(score, file)


with open("test02.txt", "rb") as file:
    score = pickle.load(file)
    print(score)

print(score)    # with 내 선언한 변수를 with를 호출한 범위에서 사용할 수 있음