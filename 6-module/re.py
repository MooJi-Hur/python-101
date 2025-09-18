import re

r"""
. : 문자 1개
^ : 문자열의 시작
$ : 문자열의 마지막
* : 0 or more
+ : 1 or more
? : 0 or 1
{n} : n번 반복
{n,m} : n번 부터 m번
{n,} : n번 부터 무한번
[] : 문자의 집합
| : OR
() : 괄호 안의 정규식 그룹

\w : [a-zA-Z0-9_] : a~Z, 0~9, _ 포함하는 모든 문자
\W : [^a-zA-Z0-9_] : 위의 문자 제외한 나머지 문자
\d : [0-9] : 0 부터 9
\D : [^0-9] : 숫자 제외한 나머지 문자
\s : [\t\n\r\f\v] : 공백문자
\S : [^\t\n\r\f\v] : 공백 제외한 모든 문자
\b : 단어의 시작과 끝의 빈 공백
\B : 단어의 시작과 끝이 아닌 빈 공백
\\ : \
\[숫자] : 지정된 숫자만큼 일치하는 문자열
\A : 문자열의 시작
\Z : 문자열의 끝
"""

# 정규 표현식 regex regular expression
txt = "This module provides regular expression matching operations similar to those found in Perl."
print(txt)
# *

# 처음 찾은 결과 하나를 가져옴
match_txt = re.match(r"[a-zA-Z]*", txt)
print(match_txt)
print(match_txt.group(0))   # 공백이 나와서 멈춤

search_txt = re.search(r"[\w]*", txt)
print(search_txt)   # 객체 반환
print(search_txt.group(0))

# 전체 결과
findall_txt = re.findall(r"[a-zA-Z]*", txt)
print(findall_txt)  # 리스트로 반환   # 해당하지 않는 그룹은 빈 문자열로 처리했음

# t찾기
find_t_txt = re.findall(r"T[a-zA-Z]*", txt)
print(find_t_txt)

find_rr_txt = re.findall(r"r[a-zA-Z]+r", txt)
print(find_rr_txt)


# o로 시작하면서 s로 끝나는 단어
find_os_txt = re.findall(r"o[\w]*s", txt)
print(find_os_txt)


address="""
010-1111-1111
010-1234-5678
010-3456-7890
"""

phone_list = address.split("\n")
print(phone_list)

phone_list = list(filter(None, phone_list)) # 빈 문자열은 제거함, 필터 수행 함수가 None인 것
print(phone_list)

# replace
phone_masking = list(map(lambda x: x.replace(re.search(r"\-[0-9]*\-", x).group(0) ,"-****-"), phone_list))
print(phone_masking)

