def history():
    read_h = input('\nWould you like to see your game scores? Y or N :')
    if read_h == 'Y':
        file = open('scores.txt', 'r')
        previous_scores = file.read()
        print(previous_scores)
        file.close()
        
    else:
        print('\nOk thank you for playing')