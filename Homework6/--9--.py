days = int(input())
room = input()
grade = input()
nights = days - 1

if room == 'room for one person':
    total = nights * 18
elif room == 'apartment':
    total = nights * 25
    if days < 10:
        total *= 0.7
    elif 10 <= days <= 15:
        total *= 0.65
    elif 15 < days:
        total *= 0.5
elif room == 'president apartment':
    total = nights * 35
    if days < 10:
        total *= 0.9
    elif 10 <= days <= 15:
        total *= 0.85
    elif 15 < days:
        total *= 0.8

if grade == 'positive':
    total += total * 0.25
    print(f'{total:.2f}')
else:
    total -= total * 0.1
    print(f'{total:.2f}')