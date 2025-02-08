n = int(input())
k = int(input())

prime = [0] * (n+1)

for i in range(2, n+1):
    if prime[i] == 0:
        for j in range(i, n+1, i):
            if j % i == 0:
                prime[j] = max(prime[j], i)

ans = 0
for i in prime:
    if i <= k:
        ans += 1
print(ans - 1)

#참고하긴 했는데, 솔직하게 잘 이해되지 않음
