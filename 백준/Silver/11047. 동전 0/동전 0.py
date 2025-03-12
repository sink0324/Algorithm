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