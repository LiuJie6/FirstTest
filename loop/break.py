while True:
    guess = input('Enter something:')
    if guess == 'quit':
        break
    print(guess+'the string\' length is', len(guess))
print('Done')
