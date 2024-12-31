n, l, d = map(int, input().split())

total = n * l + (n-1) * 5
song = [False] * total

for i in range(0, total, l+5):
    for j in range(i, i+l):
        song[j] = True
for i in range(0, total, d):
    if not song[i]:
        print(i)
        break
else:
    print(i + d)

#조금 더 생각을 잘 해보기
#전체 시간 배열을 가지고 하는 게 더 편하다. 일부 구간에서만 가능한지 확인하면, 예외와 반례가 너무 많아짐.
