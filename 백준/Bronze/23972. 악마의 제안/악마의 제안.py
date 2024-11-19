k, n = map(int, input().split())

if n == 1:
    print(-1)
else:
    x = (k * n) // (n-1)
    if (x - k) * n < x: x += 1
    print(x)

