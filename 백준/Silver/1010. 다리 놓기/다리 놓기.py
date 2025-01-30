t = int(input())
bridge = [[0] * 30 for _ in range(30)]
for i in range(30):
    for j in range(30):
        if i == 1:
            bridge[i][j] = j
        else:
            if i == j:
                bridge[i][j] = 1
            elif i < j:
                bridge[i][j] = bridge[i-1][j-1] + bridge[i][j-1]
for _ in range(t):
    n, m = map(int, input().split())
    print(bridge[n][m])

"""import math
t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    bridge = math.factorial(m) // (math.factorial(n) * math.factorial(m-n))
    print(bridge)
"""
#dp가 아니라, 조합으로 풀이 가능함!
#블로그 참고하고서야, 조합으로 풀이가 가능한지 알았음
#dp로 푸는 경우가 있으면 1,1 부터 하나씩 해보면서 규칙을 찾아야 함!
