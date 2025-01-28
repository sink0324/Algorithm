n = int(input())

cor = []
for i in range(n):
    cor.append(list(map(int, input().split())))

cor.sort(key = lambda x : (x[0], x[1]))

for i in range(n):
    print(cor[i][0], cor[i][1])

#람다식 사용 -> lambda x : (x[0], x[1]) 이면, 앞에 걸로 비교하고, 같은 경우에 뒤에걸로 비교해서
#sort 하겠다는 의미
