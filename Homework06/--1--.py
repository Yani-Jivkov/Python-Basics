projection = input()
r = int(input())
c = int(input())

if projection == 'Premiere':
    total = r * c
    total *= 12
    print(f'{total:.2f}')
elif projection == 'Normal':
    total = r * c
    total *= 7.5
    print(f'{total:.2f}')
elif projection == 'Discount':
    total = r * c
    total *= 5
    print(f'{total:.2f}')