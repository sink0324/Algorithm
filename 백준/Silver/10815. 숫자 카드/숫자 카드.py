n = int(input())
cards = list(map(int, input().split()))
cards.sort()

m = int(input())
pred = list(map(int, input().split()))

for i in pred:
    start, end = 0, n-1
    exist = False
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] > i:
            end = mid - 1
        elif cards[mid] < i:
            start = mid + 1
        else:
            exist = True
            break
    if exist:
        print(1, end = " ")
    else:
        print(0, end =" ")

#이진탐색이라는 것을 참고함
#찾아보니, 딕셔너리로 찾으면 속도가 굉장히 빠르다고 함 
#in 연산이 for 문이랑 같은 수행시간을 가지므로, 더 빠른 속도가 필요 -> 이진 탐색 / 딕셔너리
#딕셔너리에서는 not in 등을 사용했을 때 굉장히 빠르게 탐색 가능