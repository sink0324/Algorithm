import re
import sys

strings = sys.stdin.readlines()

for i in strings:
    while 'BUG' in i:
        i = re.sub('BUG', "", i)
    print(i, end = "")
