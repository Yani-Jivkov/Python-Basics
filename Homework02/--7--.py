chiken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())
chiken_menu_price = chiken_menu * 10.35
fish_menu_price = fish_menu * 12.40
vegan_menu_price = vegan_menu * 8.15
total = chiken_menu_price + fish_menu_price + vegan_menu_price
total = total + (total / 5)
total = total + 2.5

print(total)