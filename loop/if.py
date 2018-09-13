number = 20
guess = int(input('Enter an integer number:'))

if number == guess:
    print('相等')
elif guess > number:
    print('输入过大')
else:
    print('输入过小')
