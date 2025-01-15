n = int(input())
vote = [0] * 3
vote_pow = [0] *3

for i in range(n):
    first, sec, third = list(map(int, input().split()))
    #각 점수 더하기
    vote[0] += first
    vote[1] += sec
    vote[2] += third

    #제곱 점수 더하기
    vote_pow[0] += first*first
    vote_pow[1] += sec*sec
    vote_pow[2] += third*third

m = max(vote)
if vote.count(m) == 1:
    for i in range(3):
        if vote[i] == m:
            print(i+1, m)
            break
else:
    m2 = max(vote_pow)
    if vote_pow.count(m2) == 1:
        print(vote_pow.index(m2)+1, m)
    else:
        print(0, m)

#블로그 참고함
#개수를 비교할 때, 제곱을 이용하면 비교가 더 쉬워지는 장점이 있다. 제곱을 이용해보자