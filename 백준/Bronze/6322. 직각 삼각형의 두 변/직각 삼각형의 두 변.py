import math

cnt = 1
while True:
    a, b, c = map(int, input().split())
    if (a == 0) and (b == 0) and (c == 0):
        break
    
    print("Triangle #{}".format(cnt))
    if (c == -1):
        c = math.sqrt(a**2 + b**2)
        print("c = {:.3f}".format(c))
    elif (a < c) and (b < c):
        if a == -1:
            a = math.sqrt(c**2 - b**2)
            print("a = {:.3f}".format(a))
        elif b == -1:
            b = math.sqrt(c**2 - a**2)
            print("b = {:.3f}".format(b))
        else:
            print("Impossible.")
    else:
        print("Impossible.")
    print()
    cnt += 1

#gpt의 도움을 조금은 받긴 했으나, 거의 안 받음
#cnt 증가를 매 조건문 마다 했는데 오류
#print('\n')을 했는데, 그게 오류의 원인이 되었음 -> '출력 형식이 잘못 되었음' 
#코드의 중복이나 비효율성을 고려할 수 있는 문제였다고 생각함!!
