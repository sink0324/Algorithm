room = input()
num_lst = [0 for _ in range(10)]

for i in range(len(room)):
    if (room[i] == '9') or (room[i] == '6'):
        num_lst[6] += 1
    else:
        num_lst[int(room[i])] += 1

if num_lst[6] % 2 == 0:
    num_lst[6] = num_lst[6] // 2
    print(max(num_lst))
else:
    num_lst[6] = (num_lst[6] // 2 ) + 1
    print(max(num_lst))