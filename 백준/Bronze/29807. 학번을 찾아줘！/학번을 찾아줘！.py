n = int(input())
scores = list(map(int, input().split()))

for i in range(5-n):
  scores.append(0)


if scores[0] > scores[2]:
  a = (scores[0] - scores[2]) * 508
else:
  a = (scores[2] - scores[0]) * 108

if scores[1] > scores[3]:
  b = (scores[1] - scores[3]) * 212
else:
  b = (scores[3] - scores[1]) * 305

if scores[4] > 0:
  c = scores[4] * 707
else:
  c = 0

stdid = (a + b + c) * 4763
print(stdid)