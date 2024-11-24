n = int(input())
top = list(map(int, input().split()))
cnt = 1

for i in range(n-1):
    if len(top) == 1: break
    if top[i] <= top[i+1]:
        cnt += 1
    else:
        continue
print(cnt)