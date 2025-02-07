n = int(input())
dasom = int(input())

candidate = []
cnt = 0
idx = 1

for i in range(n-1):
    candidate.append(int(input()))

if n == 1:
    print(0)
elif (candidate.count(max(candidate)) == n):
    print(1)
else:
    while True :
        if max(candidate) >= dasom:
            candidate[candidate.index(max(candidate))] -= 1
            dasom += 1
            cnt += 1
        if dasom > max(candidate):
            break
    print(cnt)
