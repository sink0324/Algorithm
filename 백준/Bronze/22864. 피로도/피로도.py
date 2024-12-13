a, b, c, m = map(int, input().split())

tired = 0
work = 0

for _ in range(24):
    if (tired + a) <= m:
        work += b
        tired += a
    elif (tired + a) > m:
        tired -= c
    
    if tired < 0:
        tired = 0

print(work)