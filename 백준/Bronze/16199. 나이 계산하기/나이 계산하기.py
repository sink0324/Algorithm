birth = list(map(int, input().split()))
std = list(map(int, input().split()))

man_age = 0
cnt_age = 1
year_age = 0

if std[0] - birth[0] <= 0:
  print(man_age)
  print(cnt_age)
  print(year_age)
elif std[0] - birth[0] > 0:
  if (std[1] - birth[1] < 0) or ((std[1] - birth[1] == 0) and (std[2] - birth[2] < 0)):
    print(man_age + (std[0] - birth[0] -1))
    print(cnt_age + (std[0] - birth[0]))
    print(year_age + (std[0] - birth[0]))
  else:
    print(man_age + (std[0] - birth[0]))
    print(cnt_age + (std[0] - birth[0]))
    print(year_age + (std[0] - birth[0]))
