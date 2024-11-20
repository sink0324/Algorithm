import math

cnt = 1
while True:
    a, b, c = map(int, input().split())
    if (a == 0) and (b == 0) and (c == 0):
        break
    
    print("Triangle #{}".format(cnt))
    if (c == -1):
        c = math.sqrt(a**2 + b**2)
        print("c = {:.3f}".format(c))
    elif (a < c) and (b < c):
        if a == -1:
            a = math.sqrt(c**2 - b**2)
            print("a = {:.3f}".format(a))
        elif b == -1:
            b = math.sqrt(c**2 - a**2)
            print("b = {:.3f}".format(b))
        else:
            print("Impossible.")
    else:
        print("Impossible.")
    print()
    cnt += 1
