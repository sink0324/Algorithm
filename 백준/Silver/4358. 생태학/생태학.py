import sys
input = sys.stdin.readline

word = {}
n = 0
while True:
    tree = str(input().rstrip())

    if not tree:
        break

    if tree in word:
        word[tree] += 1
    else:
        word[tree] = 1
    n+=1

trees = list(word.keys())
trees.sort()
for i in trees:
    pct = (word[i] / n) * 100
    print(f"{i} {pct:.4f}")

#소수점 ~자리인 경우 format 사용하기
