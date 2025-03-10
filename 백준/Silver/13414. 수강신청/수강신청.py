import sys
input = sys.stdin.readline

K, L = map(int, input().split())
std_dic = dict()

for i in range(L+1):
    std_id = input().rstrip()
    std_dic[std_id] = i

std_dic = dict(sorted(std_dic.items(), key = lambda x : x[1]))

cnt = 0
for i in std_dic.keys():
    print(i)
    cnt += 1
    if cnt == K:
        break

#블로그 참고함
#중복이 없어야 하는 경우, set도 있지만, dictionary도 있다는 것을 잊지말자.
#lambda 식을 잘 이용하자.
