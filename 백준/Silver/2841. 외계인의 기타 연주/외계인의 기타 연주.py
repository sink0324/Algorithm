import sys
input = sys.stdin.readline

N, P = map(int, input().split())
melody = [[] for _ in range(7)]
cnt = 0

for _ in range(N):
    string, fret = map(int, input().split())
    if not melody[string]:
        melody[string].append(fret)
        cnt += 1
    
    else:
        while melody[string] and melody[string][-1] > fret:
                melody[string].pop()
                cnt += 1
        if melody[string] and melody[string][-1] == fret:
                continue
        melody[string].append(fret)
        cnt += 1
print(cnt)