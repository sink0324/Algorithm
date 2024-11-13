string = input()

#질문 게시판을 통해 반례 학습
if (string[0] == '"') and (string[-1] == '"') and (len(string[1:-1]) > 0):
  print(string[1:-1])
else:
  print("CE")