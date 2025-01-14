while True:
    try:
        dots = list(map(float, input().split()))

        dot1 = [dots[0], dots[1]]
        dot2 = [dots[2], dots[3]]
        dot3 = [dots[4], dots[5]]
        dot4 = [dots[6], dots[7]]

        while True:
            if dot2 == dot3:
                break
            dot1, dot2 = dot2, dot1
            if dot2 == dot3:
                break
            dot1, dot2 = dot2, dot1
            dot3, dot4 = dot4, dot3
        
        x = dot2[0] - (dot1[0] + dot4[0])
        y = dot2[1] - (dot1[1] + dot4[1])

        if x != 0:
            x = -x
        if y != 0:
            y = -y
        
        print(f"{x:.3f} {y:.3f}")
    except:
        break


#블로그와 게시판을 참고함
#입력을 끊임없이 받아야 하는 경우, try-except문을 이용하여 예외 발생 시 break 하도록 함
#너무 어려웠음ㅜ.ㅜ
