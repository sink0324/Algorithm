n = int(input())

words = []
for i in range(n):
    words.append(input())

words = set(words)
words = list(words)
words.sort()
words.sort(key = len)

for i in words:
    print(i)

#sort는 parameter로 key를 지정해줌으로써 sort의 기준점을 지정해줄 수 있음!
#중복을 제거하기 위해서는 set은 쓰자!
#정렬할 때, 작은 기준으로 먼저 정렬하면 순서가 다시 바뀜
#블로그 참고함
#cf) sorted()는 mutable 하지 않음