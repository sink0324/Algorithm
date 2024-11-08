rising = 0
diving = 0
constant = 0

fish = [int(input()) for _ in range(4)]
for i in range(3):
  if fish[i+1] > fish[i]:
    rising += 1
  elif fish[i+1] < fish[i]:
    diving +=1
  elif fish[i+1] == fish[1]:
    constant += 1

if rising == 3:
  print("Fish Rising")
elif diving == 3:
  print("Fish Diving")
elif constant == 3:
  print("Fish At Constant Depth")
else:
  print("No Fish")