fruit = input()
day = input()
count = float(input())

if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit == 'banana':
        print(f'{(count * 2.5):.2f}')
    elif fruit == 'apple':
        print(f'{(count * 1.2):.2f}')
    elif fruit == 'orange':
        print(f'{(count * 0.85):.2f}')
    elif fruit == 'grapefruit':
        print(f'{(count * 1.45):.2f}')
    elif fruit == 'kiwi':
        print(f'{(count * 2.7):.2f}')
    elif fruit == 'pineapple':
        print(f'{(count * 5.5):.2f}')
    elif fruit == 'grapes':
        print(f'{(count * 3.85):.2f}')
    else:
        print('error')
elif day in ['Saturday', 'Sunday']:
    if fruit == 'banana':
        print(f'{(count * 2.7):.2f}')
    elif fruit == 'apple':
        print(f'{(count * 1.25):.2f}')
    elif fruit == 'orange':
        print(f'{(count * 0.9):.2f}')
    elif fruit == 'grapefruit':
        print(f'{(count * 1.6):.2f}')
    elif fruit == 'kiwi':
        print(f'{(count * 3):.2f}')
    elif fruit == 'pineapple':
        print(f'{(count * 5.6):.2f}')
    elif fruit == 'grapes':
        print(f'{(count * 4.2):.2f}')
    else:
        print('error')
elif day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
    print('error')