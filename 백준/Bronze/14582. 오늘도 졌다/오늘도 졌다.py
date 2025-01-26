geminis = list(map(int, input().split()))
startlink = list(map(int, input().split()))

gem_score = 0
st_score = 0
victory = False

if sum(geminis) >= sum(startlink):
    print("No")
else:
    for i in range(len(geminis)):
        gem_score += geminis[i]
        if gem_score > st_score:
            victory = True
        st_score += startlink[i]
    if victory:
        print("Yes")
    else:
        print("No")

#게시판 약간 참고함