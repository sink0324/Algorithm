n = int(input())
n_num = list(map(int, input().split()))
m = int(input())
m_num = list(map(int, input().split()))

n_num.sort()

for i in m_num:
    start = 0
    end = n-1
    exist = False

    while start <= end:
        mid = (start + end) // 2
        if n_num[mid] > i:
            end = mid - 1
        elif n_num[mid] < i:
            start = mid + 1
        else:
            exist = True
            break
    if exist:
        print(1)
    else:
        print(0)
    