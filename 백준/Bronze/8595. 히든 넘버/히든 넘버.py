import re

wlen = int(input())
word = input()
pattern = r'\d+'

res = re.findall(pattern, word)

for i in range(len(res)):
    res[i] = int(res[i])

if len(res) == 0:
    print(0)
else:
    print(sum(res))

#'\d' : 숫자와 매치 / '\w' : 숫자를 포함한 모든 문자와 매치
#findall은 패턴에 맞는 게 있으면 전부 찾아서 리스트로 저장함 -> 숫자를 모두 저장
#여기서 뒤에 +를 붙여야 모여있는 숫자를 전부 찾아냄. 만약 뒤에 +가 없다면, 숫자를 하나하나 추출
#정규포현식은 한 번 공부하는 것이 중요할듯함
