def start():
    file = open('scores.txt', 'w')
    file.write('\nThis is your dice roller history')
    
    user = input('What is your name?')
    file.write('\nWelcome ' + user)
    print('These are your scores:')
    file.close()
    