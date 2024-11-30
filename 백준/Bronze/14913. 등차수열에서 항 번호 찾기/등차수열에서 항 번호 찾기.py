a, d, k = map(int, input().split())


if (k - a) % d == 0 and (k - a) // d >= 0:
    res = (k - a) // d + 1
    print(res)
else:
    print("X")

#블로그 참고했음
#왜인지 머리가 안 돌아감..