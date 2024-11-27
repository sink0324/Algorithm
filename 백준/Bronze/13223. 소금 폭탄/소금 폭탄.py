current = list(map(int, input().split(':')))
salt = list(map(int, input().split(':')))

cur_total = current[0] * 3600 + current[1] * 60 + current[2]

salt_total = salt[0] * 3600 + salt[1] * 60 + salt[2]
    
diff = salt_total - cur_total

if diff <= 0:
    diff += 24 * 3600

hh = diff // 3600
mm = (diff % 3600) // 60
ss = diff % 60

print("{0:02d}:{1:02d}:{2:02d}".format(hh, mm, ss))

#format을 사용할 때, 콜론 앞을 인덱스에 맞게 변경해야 올바른 값이 들어감
#zfill 사용하는 것 추천