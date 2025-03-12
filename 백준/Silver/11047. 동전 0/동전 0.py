import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin_val = list()
cnt = 0

for i in range(N):
    coin_val.append(int(input()))

coin_val.sort(reverse=True)

for coin in coin_val:
    if K >= coin:
        cnt += K//coin
        K %= coin
        if K <= 0:
            break

print(cnt)

#나누면 되는데, 복잡하게 생각했었음. 동전 문제는 보통 나눗셈 하면 되는듯!
#블로그 조금 참고함
