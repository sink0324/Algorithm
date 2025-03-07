import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append(idx + 1)

    if paper > 0:
        q.rotate(-(paper - 1))
    elif paper < 0:
        q.rotate(-paper)

print(' '.join(map(str, ans)))

#블로그 참고함 -> deque 구조 이해
#rotate는 deque와 함께 이용했을 때 효용이 높아진다.
