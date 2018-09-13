number = 20
running = True

while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print('猜对了')
        running = False
    else:
        print('猜错了')
else:
    print('执行完成')
