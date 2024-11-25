from sys import stdin

for i in range(3):
    n = int(input())
    li = [int(stdin.readline()) for i in range(n)]
    if sum(li) == 0: print(0)
    elif sum(li) < 0: print('-')
    elif sum(li) > 0: print('+')

"""from sys import stdin

for i in range(3):
    n = int(input())
    li = [int(stdin.readline()) for i in range(n)]
    if sum(li) == 0: print(0)
    elif sum(li) < 0: print('-')
    elif sum(li) > 0: print('+')"""
=> 위의 코드가 성공은 했지만om sys import stdin

for i in range(3):
    n = int(input())
    li = [int(stdin.readline()) for i in range(n)]
    if sum(li) == 0: print(0)
    elif sum(li) < 0: print('-')
    elif sum(li) > 0: print('+')

"""from sys import stdin

for i in range(3):
    n = int(input())
    li = [int(stdin.readline()) for i in range(n)]
    if sum(li) == 0: print(0)
    elif sum(li) < 0: print('-')
    elif sum(li) > 0: print('+')"""
#=> 위의 코드가 성공은 했지만, 기존 코드의 수행시간은 7704ms이고, 주석으로 추가한 코드의 수행시간은 180ms였다.
#무려 42배의 성능 차이가 있었음을 알 수 있다. -> 만약 시간이 없었다면 시간 초과를 받았을 것
#stdin을 통해 readline()을 수행하면 더 빠르게 라인을 읽을 수 있으므로 더 빠른 성능을 낼 수 있다 -> 자바의 bufferedreader 같음
#방중에 stdin에 관한 레퍼런스를 찾아보는 것도 좋을 듯하다.
