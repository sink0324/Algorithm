board = input()

board = board.replace('XXXX', 'AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)

#해결 안 돼서 보라 코드 봄 - 보라 감사
#while문으로 인덱스를 올려주면서 검사하는 방법이 있다. [idx:idx+4] 이런 식으로
    