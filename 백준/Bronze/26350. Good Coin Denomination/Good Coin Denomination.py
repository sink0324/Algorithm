num = int(input())

for i in range(num):
  res = False
  n, *d = map(int, input().split())
  for j in range(1, n):
    if d[j] < d[j-1]*2:
      break
  else: res = True
  print("Denominations:", *d)
  if res : print("Good coin denominations!", '\n')
  else : print("Bad coin denominations!", '\n')
