n = int(input())
left = 1
right = 1
tropy = [int(input()) for _ in range(n)]
left_max = tropy[0]
right_max = tropy[n-1]

for i in range(n):
    if left_max < tropy[i]:
        left_max = tropy[i]
        left += 1
for i in range(n):
    if right_max < tropy[(n-1)-i]:
        right_max = tropy[(n-1)-i]
        right += 1
print(left)
print(right)