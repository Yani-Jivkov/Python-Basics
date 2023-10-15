flower_type = input()
flowers_count = int(input())
budget = int(input())
total = 0


if flower_type == 'Roses':
    if 80 < flowers_count:
        total = flowers_count * 5
        total *= 0.1
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')
    else:
        total = flowers_count * 5
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')
elif flower_type == 'Dahlias':
    if 90 < flowers_count:
        total = flowers_count * 3.8
        total *= 0.15
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')
    else:
        total = flowers_count * 3.8
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')
elif flower_type == 'Tulips':
    if 80 < flowers_count:
        total = flowers_count * 2.8
        total *= 0.15
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')
    else:
        total = flowers_count * 2.8
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')
elif flower_type == 'Narcissus':
    if 80 < flowers_count:
        total = flowers_count * 3
        total += (total * 0.85)
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')
    else:
        total = flowers_count * 3
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')
elif flower_type == 'Gladiolus':
    if 80 < flowers_count:
        total = flowers_count * 2.5
        total += (total * 0.8)
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')
    else:
        total = flowers_count * 2.5
        if budget > total:
            print(
                f'Hey, you have a great garden with {flowers_count} {flower_type} and {(budget - total):.2f} leva left.')
        else:
            print(f'Not enough money, you need {(total - budget):.2f} leva more.')

