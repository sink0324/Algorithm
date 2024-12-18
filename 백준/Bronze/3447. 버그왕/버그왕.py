import re
import sys

strings = sys.stdin.readlines()

for i in strings:
    while 'BUG' in i:
        i = re.sub('BUG', "", i)
    print(i, end = "")

#파일 입출력 같은 경우는, 끝이 없는 경우 vs에서 입력이 안 끝날 수도 있음
#re는 정규표현식 라이브러리 -> 문자열 내의 패턴을 검색, 제거, 치환 가능
#정규식 객체를 생성하여, 패턴에 따라 문자열을 조절 가능
