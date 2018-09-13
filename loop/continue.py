while True:
    s = input("Enter something:")
    if s == 'quit':
        break
    elif len(s) < 3:
        print('s太小了')
        continue
    print(s, len(s))
print('Done')
