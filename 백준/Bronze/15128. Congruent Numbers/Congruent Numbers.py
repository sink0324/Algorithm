nums = list(map(int, input().split()))
area = nums[0] / nums[1] * nums[2] / nums[3] / 2

if int(area) == area:
  area = int(area)
if isinstance(area, int):
  print(1)
else:
  print(0)