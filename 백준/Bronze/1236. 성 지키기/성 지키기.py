row, col = map(int, input().split())

col_li = [False] * col
row_li = [False] * row
need_col = 0
need_row = 0

castle = [list(input()) for _ in range(row)]

for rows in range(row):
    for cols in range(col):
        if castle[rows][cols] == 'X':
            col_li[cols] = True
            row_li[rows] = True

for cols in range(col):
    if col_li[cols] is False:
        need_col += 1
for rows in range(row):
    if row_li[rows] is False:
        need_row += 1

print(max(need_row, need_col))