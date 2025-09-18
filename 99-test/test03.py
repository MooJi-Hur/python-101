# 반복문과 lambda를 사용하여 학생 각각의 총점과 평균을 출력하자
import math

students = [{'name': '홍길동', 'kor': 100, 'eng': 70, 'math': 89},
            {'name': '이순신', 'kor': 66, 'eng': 87, 'math': 100},
            {'name': '김선달', 'kor': 91, 'eng': 100, 'math': 84}]

totals = [ student['kor'] + student['eng'] + student['math'] for student in students]
print(totals)
avgs = list(map(lambda x: x,totals))

for index, student in enumerate(students):
    # total = student['kor'] + student['eng'] + student['math']
    # avg = total / 3

    print(f"[{student['name']}]\n총점 : {totals[index]}\t평균 : {avgs[index]:.2f}")


'''
출력결과

[홍길동]
총점 : 259 	 평균 : 86.33
[이순신]
총점 : 253 	 평균 : 84.33
[김선달]
총점 : 275 	 평균 : 91.67
'''




