nums = list(map(int, input().split()))

num1 = nums[0]
num2 = nums[1]
num3 = nums[2]

ans1 = int(num1 * num2 / num3)
ans2 = int(num1 / num2 * num3)

if ans1 >= ans2:
    print(ans1)
else:
    print(ans2)