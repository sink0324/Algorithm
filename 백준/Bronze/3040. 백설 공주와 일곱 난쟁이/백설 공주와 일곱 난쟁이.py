dwarf = [int(input()) for _ in range(9)]
total = sum(dwarf)

for i in range(8):
    for j in range(i+1, 9):
        if (total - dwarf[i] - dwarf[j]) == 100:
            fake1 = dwarf[i]
            fake2 = dwarf[j]
            break
    if len(dwarf) == 7:
        break
dwarf.remove(fake1)
dwarf.remove(fake2)

for k in range(7):
    print(dwarf[k])