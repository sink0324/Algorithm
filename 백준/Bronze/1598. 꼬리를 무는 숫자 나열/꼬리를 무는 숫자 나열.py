import math
a, b = map(int, input().split())

a_pos = a % 4
b_pos = b % 4

if (a_pos == 0):
    a_pos = 4
if (b_pos == 0):
    b_pos = 4

row_dis = abs(a_pos - b_pos)
col_dis = abs(math.ceil(b/4) - math.ceil(a/4))
print(row_dis + col_dis)