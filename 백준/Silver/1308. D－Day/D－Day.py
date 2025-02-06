import datetime

today = list(map(int, input().split()))
dday = list(map(int, input().split()))

today_ = datetime.date(today[0], today[1], today[2])
dday_ = datetime.date(dday[0], dday[1], dday[2])

if today[0] + 1000 < dday[0]:
    print("gg")
elif today[0] + 1000 == dday[0] and (today[1], today[2]) <= (dday[1], dday[2]):
    print("gg")
else:
    print("D-" + str(dday_.toordinal() - today_.toordinal()))

#datetime을 이용하면 날짜 간 계산을 편리하게 할 수 있다.
#toordinal()을 이용하면 1년 1월 1일부터 누적 날짜이므로 윤년 포함되어 있음
#.days를 이용하면 날짜만 구할 수 있음