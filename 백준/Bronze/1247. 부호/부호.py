for i in range(3):
    n = int(input())
    s = 0
    for j in range(n):
        integer = int(input())
        s += integer
    if s == 0: print(0)
    elif s < 0: print('-')
    elif s > 0: print('+')