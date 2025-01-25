n = int(input())
m = input()
k = int(input())

if ('1' not in m) or (k == 0):
    print("YES")
    exit(0)

count = 0

for i in range(len(m)-1, -1, -1):
    if m[i] == '1':
        break
    if m[i] == '0':
        count += 1

if count >= k:
    print("YES")
else:
    print("NO")

#만약 110000 이라면, 2^4(2^1 + 2^0)이 됨 -> 무조건 나누어 떨어지게 되는 것