import math
n = int(input())

sum = 0

for i in range(n):
    score = int(input())
    if (score % 10) == 6 or (score % 10) == 0:
        score = score - score%10 + 9
    if (score // 10) == 6:
        score = 90 + (score % 10)
    if score >= 100:
        score = 100
    sum += score
avg = sum / n

if avg - int(avg) >= 0.5: print(math.ceil(avg))
else: print(math.floor(avg))