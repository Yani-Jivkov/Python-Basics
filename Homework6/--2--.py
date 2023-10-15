degrees = int(input())
time = input()

if time == 'Morning':
    if 10 <= degrees <= 18:
        wear = 'Sweatshirt'
        shoes = 'Sneakers'
        print(f'It\'s {degrees} degrees, get your {wear} and {shoes}.')
    elif 18 < degrees <= 24:
        wear = 'Shirt'
        shoes = 'Moccasins'
        print(f'It\'s {degrees} degrees, get your {wear} and {shoes}.')
    elif degrees >= 25:
        wear = 'T-Shirt'
        shoes = 'Sandals'
        print(f'It\'s {degrees} degrees, get your {wear} and {shoes}.')
elif time == 'Afternoon':
    if 10 <= degrees <= 18:
        wear = 'Shirt'
        shoes = 'Moccasins'
        print(f'It\'s {degrees} degrees, get your {wear} and {shoes}.')
    elif 18 < degrees <= 24:
        wear = 'T-Shirt'
        shoes = 'Sandals'
        print(f'It\'s {degrees} degrees, get your {wear} and {shoes}.')
    elif degrees >= 25:
        wear = 'Swim Suit'
        shoes = 'Barefoot'
        print(f'It\'s {degrees} degrees, get your {wear} and {shoes}.')
elif time == 'Evening':
        if 10 <= degrees <= 18:
            wear = 'Shirt'
            shoes = 'Moccasins'
            print(f'It\'s {degrees} degrees, get your {wear} and {shoes}.')
        elif 18 < degrees <= 24:
            wear = 'Shirt'
            shoes = 'Moccasins'
            print(f'It\'s {degrees} degrees, get your {wear} and {shoes}.')
        elif degrees >= 25:
            wear = 'Shirt'
            shoes = 'Moccasins'
            print(f'It\'s {degrees} degrees, get your {wear} and {shoes}.')