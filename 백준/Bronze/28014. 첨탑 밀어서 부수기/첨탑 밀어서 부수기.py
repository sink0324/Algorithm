n = int(input())
top = list(map(int, input().split()))
cnt = 1

for i in range(n-1):
    if len(top) == 1: break
    if top[i] <= top[i+1]: #<= 이어야 함. 같아도 넘어지지 않기 때문. 부등호를 잘 생각하자.
        cnt += 1
    else:
        continue
print(cnt)
