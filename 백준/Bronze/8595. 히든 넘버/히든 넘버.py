import re

wlen = int(input())
word = input()
pattern = r'\d+'

res = re.findall(pattern, word)

for i in range(len(res)):
    res[i] = int(res[i])

if len(res) == 0:
    print(0)
else:
    print(sum(res))