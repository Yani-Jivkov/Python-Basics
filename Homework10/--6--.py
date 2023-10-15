h = int(input())
w = int(input())
pieses = h * w
total = 0

while True:
    text = input()
    if text == 'STOP':
        if total >= pieses:
            print(f'No more cake left! You need {total - pieses} pieces more.')
            break
        else:
            print(f'{pieses - total} pieces are left.')
            break

    piessess = int(text)
    total += piessess

    if total >= pieses:
        print(f'No more cake left! You need {total - pieses} pieces more.')
        break
else:
    print(f'{pieses - total} pieces are left.')