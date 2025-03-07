import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    note1 = set(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    for i in note2:
        if i in note1:
            print(1)
        else:
            print(0)

#set은 list보다 탐색속도가 더 빠르다. 그러므로 set으로 입력받을 수 있다면 set으로 입력받자.
#set의 수행시간은 O(1)
