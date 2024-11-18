k, l = map(int, input().split())

for i in range(2, l):
    if k % i == 0:
        print("BAD", i)
        break
else:
    print("GOOD")

#블로그 참고함
#어차피 어떤 수가 주어지더라도 l보다 큰지 작은지만 보므로, 그 이상의 숫자는 신경쓸 필요 없음
#실제로 어떤 수의 곱인지는 중요하지 않고, l보다 큰지 여부만 확인하므로 코드는 간단 - 알고리즘을 생각하는 게 어렵다! 
#알고리즘적 사고를 키우자.
