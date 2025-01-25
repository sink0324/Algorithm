while True:
    word = input()
    correct = True
    
    if word == '#': 
        break
    
    while True:
        changed = input()
        count = 0

        if changed == '#': 
            break

        if len(word) != len(changed):
            correct = False
        else:
            for i in range(len(word)):
                if word[i] != changed[i]:
                    count += 1
            if count != 1:
                correct = False

        word = changed
    
    if correct:
        print("Correct")
    else:
        print("Incorrect")