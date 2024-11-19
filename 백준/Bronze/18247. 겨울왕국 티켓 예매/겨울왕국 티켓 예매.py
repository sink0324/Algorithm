n = int(input())

for i in range(n):
    row, col = map(int, input().split())
    if row >= 12 and col >= 4:
        seat = 11 * col + 4
        print(seat)
    else:
        print(-1)