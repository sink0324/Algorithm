from sys import stdin

t = int(input())
li = [0]
for i in range(t):
    a, b = map(int, stdin.readline().split())
    a %= 10
    if a == 0:
        print(10)
    elif (a == 1) or (a == 5) or (a == 6):
        print(a)
    elif (a == 4) or (a == 9):
        if b % 2 ==0:
            print(a**2 % 10)
        else:
            print(a)
    else:
        if b % 4 == 0:
            print(a**4 % 10)
        else:
            print(a**(b%4) % 10)

#블로그 참고함 -> 경우의 수를 나누자
#뭔가 고민이 필요할 것 같음. 경우의 수를 나누는 게 가장 중요한듯.
