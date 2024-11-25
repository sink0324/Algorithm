from sys import stdin

for i in range(3):
    n = int(input())
    li = [int(stdin.readline()) for i in range(n)]
    if sum(li) == 0: print(0)
    elif sum(li) < 0: print('-')
    elif sum(li) > 0: print('+')