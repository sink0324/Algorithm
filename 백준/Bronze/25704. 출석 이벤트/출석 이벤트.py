attd = [int(input()) for _ in range(2)]
stamp = attd[0]
price = attd[1]
dc = []

if 5 <= stamp < 10:
    dc.append(price-500)
elif 10 <= stamp < 15:
    dc.append(price-500)
    dc.append(price*0.9)
elif 15 <= stamp < 20:
    dc.append(price*0.9)
    dc.append(price-2000)
elif 20 <= stamp:
    dc.append(price-2000)
    dc.append(price*0.75)

if dc:
    price = min(dc)
    
if price < 0:
    print(0)
else:
    print(int(price))