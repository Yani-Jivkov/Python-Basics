film_buged = float(input())
peaople_count = int(input())
price_for_clothes = float(input())
full_price_for_clothes = peaople_count * price_for_clothes
decor = film_buged / 10
expenses = decor

if peaople_count > 150:
    full_price_for_clothes = full_price_for_clothes - (full_price_for_clothes / 10)
    expenses = expenses + full_price_for_clothes
else:
    expenses = expenses + full_price_for_clothes

if expenses > film_buged:
    print('Not enough money!')
    print(f'Wingard needs {expenses - film_buged:.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {film_buged - expenses:.2f} leva left.')
