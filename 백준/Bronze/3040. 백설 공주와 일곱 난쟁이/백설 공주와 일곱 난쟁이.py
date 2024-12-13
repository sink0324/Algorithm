dwarf = [int(input()) for _ in range(9)]
total = sum(dwarf)

for i in range(8):
    for j in range(i+1, 9):
        if (total - dwarf[i] - dwarf[j]) == 100:
            fake1 = dwarf[i]
            fake2 = dwarf[j]
            break
    if len(dwarf) == 7:
        break
dwarf.remove(fake1)
dwarf.remove(fake2)

for k in range(7):
    print(dwarf[k])

#블로그를 참고함
#배열의 인덱스 문제 -> 인덱스를 하나하나 생각하면서 보기 - 특히 인덱스가 감소하는 경우!!
#변수에 저장했다가 인덱스 이슈 없을 만한 곳에서 없애도 됨
