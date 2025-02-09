n = int(input())

for i in range(n):
    std_id = []
    g = int(input())

    for j in range(g):
        std_id.append(int(input()))

    if g == 1:
        print(1)
    else:
        cnt = 2
        while True:
            mod = []
            for k in range(g):
                mod.append(std_id[k] % cnt)
            mod = set(mod)
            mod = list(mod)
            if len(mod) == len(std_id):
                print(cnt)
                break
            else:
                cnt += 1

#블로그 참고함
#일일이 나눠야 한다고 생각했었지만, 결과적으로 나머지가 겹치지 않으면 되므로, set을 이용
#그리고 마지막에 숫자가 같으면, 서로 다른 나머지가 나왔다는 거니까 답이 도출됨                