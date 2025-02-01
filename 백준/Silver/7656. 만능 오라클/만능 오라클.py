import re
sentences = input()

start = end = -1
while sentences.find('What', end + 1) != -1:
    start = sentences.find('What', end + 1)
    end = sentences.find('?', start + 1)
    new = sentences[start:end]
    if new.find('.') != -1:
        end = sentences.find('.', start + 1)
        continue
    print('Forty-two' + new[4:] + '.')

#블로그 참고함. 문제가 별로 좋진 않은 것 같음