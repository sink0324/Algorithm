n = int(input())
nth = 666
cnt = 0

while True:
    if '666' in str(nth):
        cnt += 1
    if cnt == n:
        print(nth)
        break
    nth += 1

#문제가 이해되지 않아서 보라의 코드와 블로그를 참고함
#문제를 해석하는 게 중요하고, 브루트 포스 알고리즘은 일일이 확인하는 게 답인 것 같음