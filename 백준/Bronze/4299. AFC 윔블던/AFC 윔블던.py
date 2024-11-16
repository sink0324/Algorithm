nums = list(map(int, input().split()))

hap = nums[0]
diff = nums[1]

if (hap < diff):
    print(-1)
else:
    a = (hap + diff)//2
    b = (hap - diff)//2 
    if (a + b == hap) and (a - b == diff):
        print(a, b)
    else:
        print(-1)