col = int(input())

if col % 2 == 0:
    print("I LOVE CBNU")
else:
    print('*' * col)
    for i in range(col//2 + 1):
        if i==0:
            print(' ' * (col//2 - i) + '*')
        else:
            print(' ' * (col//2 - i) + '*' + ' ' * (2*i - 1) + '*')

