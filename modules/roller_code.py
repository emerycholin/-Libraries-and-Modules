import random

def d_roller():
    play = 1
    Round = 0
    while play == 1:
        begin = input('\nWould you like to play dice roller? Y or N :')
        if begin == 'N':
            play = 2
        elif begin == 'Y':
            
            Round = Round + 1
            print('Ok lets get started')
            print('You will get to role three dice. The goal is to add all of them up and get the highest score.\n\n')
            print('This is round ', Round)
            role1 = random.randint(1,6)
            role2 = random.randint(1,6)
            role3 = random.randint(1,6)
            
            print('Your scores were:')
            print(role1)
            print(role2)
            print(role3)
            total = role1 + role2 + role3
            print('\n Your total was: ')
            print(total)
            
            file = open('scores.txt', 'a')
            file.write('\n\nRound: ')
            file.write(str(Round))
            file.write('\nYour scores were: ')
            file.write(str(role1))
            file.write(', ')
            file.write(str(role2))
            file.write(', ')
            file.write(str(role3))
            file.write('\nYour total was: ')
            file.write(str(total))
            file.close()
d_roller()