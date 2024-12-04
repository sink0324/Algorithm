import math
n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

total = 0

for i in range(n):
    if a[i] <= b:
        total += 1
        continue
    else:
        tmp = a[i] - b
        total += 1
        total += math.ceil(tmp/c)
print(total)