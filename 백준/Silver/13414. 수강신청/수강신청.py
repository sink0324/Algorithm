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