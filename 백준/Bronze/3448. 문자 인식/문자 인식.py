from sys import stdin

n = int(input())

for i in range(n):
    sentence = ''
    for line in stdin:
        if line == '\n':
            sentence = sentence.rstrip('\n')
            break
        else:
            sentence += line.rstrip('\n')
    A = len(sentence)
    R = A - sentence.count('#')
    res = round(R/A * 100, 1)
    if str(res)[-1] == '0':
        res = int(res)

    print(f"Efficiency ratio is {res}%.")

#블로그 참고함