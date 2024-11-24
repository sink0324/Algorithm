P, k = map(int, input().split())

for i in range(2, k):
    if P % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")
#게시판 참고함
