lili_age = int(input())
washing_machine_price = float(input())
one_toy_price = int(input())
lili_money = 0
toy_money = 0
total_money = 0
savings = 0

for i in range(1, lili_age + 1):
    if i % 2 == 0:
        lili_money += 10
        savings += lili_money - 1
    else:
        toy_money += 1

toy_money *= one_toy_price
total_money = savings + toy_money

if total_money >= washing_machine_price:
    print(f'Yes! {abs(total_money - washing_machine_price):.2f}')
else:
    print(f'No! {abs(washing_machine_price - total_money):.2f}')