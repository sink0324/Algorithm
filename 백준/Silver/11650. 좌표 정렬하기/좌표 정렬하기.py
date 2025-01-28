n = int(input())

cor = []
for i in range(n):
    cor.append(list(map(int, input().split())))

cor.sort(key = lambda x : (x[0], x[1]))

for i in range(n):
    print(cor[i][0], cor[i][1])