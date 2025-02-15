import sys
string = list(sys.stdin.readline().rstrip())
command_num = int(input())

cursor = len(string)
string2 = []

for i in range(command_num):
    command = list(sys.stdin.readline().split())
    if command[0] == 'L':
        if string:
            string2.append(string.pop())

    elif command[0] == 'D':
        if string2:
            string.append(string2.pop())

    elif command[0] == 'B':
        if string:
            string.pop()
             
    else:
        string.append(command[1])

string.extend(reversed(string2))
print("".join(string))

#블로그 봤음 - 자료구조니까 큐와 스택을 적절히 잘 사용할것!