n = int(input())

students = []
candidate = [0] * n

for i in range(n):
    students.append(list(map(int, input().split())))

for i in range(n):
    for j in range(i+1, n):
        for k in range(5):
            if students[i][k] == students[j][k]:
                candidate[j] += 1
                candidate[i] += 1
                break

print(candidate.index(max(candidate)) + 1)

#구현이 어려워서 보라의 코드와 블로그를 참고함
#문제를 제대로 이해하는 게 중요함
#발상은 생각났으나, 반복문 3개를 쓰는 건 미처 생각하지 못함