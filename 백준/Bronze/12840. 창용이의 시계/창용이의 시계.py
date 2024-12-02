h, m, s = list(map(int, input().split()))
sec = h * 3600 + m * 60 + s
q = int(input())

for i in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        sec = (sec + t[1]) % 86400
    elif t[0] == 2:
        sec = (sec - t[1]) % 86400
        if sec < 0:
            sec += 86400
    elif t[0] == 3:
        print(sec//3600 , (sec%3600)//60, sec%60)