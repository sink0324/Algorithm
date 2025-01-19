n = int(input())

for _ in range(n):
    col, row = map(int, input().split())
    li = [1] * col
    for i in range(row):
        line = list(map(int, input().split()))
        for j in range(col):
            li[j] *= line[j]
    big = max(li)
    if li.count(big) == 1:
        print(li.index(big) + 1)
    else:
        multi_idx = [idx for idx, value in enumerate(li) if value == big]
        print(max(multi_idx) + 1)