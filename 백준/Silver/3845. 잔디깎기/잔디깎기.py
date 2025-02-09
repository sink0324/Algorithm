while True:
    nx, ny, w = map(float, input().split())

    if nx == 0 and ny == 0 and int(w) == 0:
        break

    xi = list(map(float, input().split()))
    yi = list(map(float, input().split()))
    nx = int(nx)
    ny = int(ny)

    
    ans = []
    lawn = True
    
    xi.sort()
    yi.sort()

    now = 0
    for i in range(nx):
        if (xi[i] - w/2) <= now:
            now = xi[i] + w/2
        else:
            lawn = False
            break
    if lawn == False or now < 75:
        ans.append("NO")

    now = 0
    for j in range(ny):
        if (yi[j] - w/2) <= now:
            now = yi[j] + w/2
        else:
            lawn = False
            break
    if lawn == False or now < 100:
        ans.append("NO")
    
    if "NO" in ans:
        print("NO")
    else:
        print("YES")

#어떻게 해결해야할지 헷갈려서 블로그를 참고함 -> 이렇게 범위가 들어가는 문제는 배열을 적용하기 
#어려워서 문제 해결에 난항이 있었음
#정수값으로 범위를 확인하면서 반복하면 된다!