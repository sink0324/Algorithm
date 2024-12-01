t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    floor = n % h
    room = n // h + 1
    if floor == 0:
        floor = h
        room -= 1    
    print(str(floor) + str((room)).zfill(2))

#블로그 참고함 -> 알고리즘이 꼬여서 제대로 안 됐음 -> 반례를 들고, 실제로 계산해보면서 확인하자.
