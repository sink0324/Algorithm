price, gram = map(int, input().split())
n = int(input())

price_list = [round(price/gram*1000, 2)]
for i in range(n):
    price_, gram_ = map(int, input().split())
    price_list.append(round(price_/gram_*1000, 2))

print(min(price_list))