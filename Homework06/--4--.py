budget = int(input())
season = input()
fishers = int(input())

if season == 'Spring':
    total = 3000
    if 6 >= fishers:
        total *= 0.9
    elif 11 >= fishers:
        total *= 0.85
    elif 12 <= fishers:
        total *= 0.75
    if (fishers % 2) == 0:
        total *= 0.95
elif season == 'Summer':
    total = 4200
    if 6 >= fishers:
        total *= 0.9
    elif 11 >= fishers:
        total *= 0.85
    elif 12 <= fishers:
        total *= 0.75
    if (fishers % 2) == 0:
        total *= 0.95
elif season == 'Autumn':
    total = 4200
    if 6 >= fishers:
        total *= 0.9
    elif 11 >= fishers:
        total *= 0.85
    elif 12 <= fishers:
        total *= 0.75
elif season == 'Winter':
    total = 2600
    if 6 >= fishers:
        total *= 0.9
    elif 11 >= fishers:
        total *= 0.85
    elif 12 <= fishers:
        total *= 0.75
    if (fishers % 2) == 0:
        total *= 0.95

if total <= budget:
    print(f'Yes! You have {(budget - total):.2f} leva left.')
else:
    print(f'Not enough money! You need {(total - budget):.2f} leva.')