n = int(input())

for _ in range(n):
    col, row = map(int, input().split())
    li = [1] * col
    for i in range(row):
        line = list(map(int, input().split()))
        for j in range(col):
            li[j] *= line[j]
    big = max(li)
    if li.count(big) == 1:
        print(li.index(big) + 1)
    else:
        multi_idx = [idx for idx, value in enumerate(li) if value == big]
        print(max(multi_idx) + 1)

#enumerate를 사용하면 복수 인덱스를 뽑는 것이 가능함
        #enumerate() : 리스트의 값과 인덱스를 함께 출력해주는 내장 함수임!
#그러나 반복문을 통해 직접 접근하는 것도 가능함!
