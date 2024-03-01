budget = float(input())
video_cards = int(input())
procesors = int(input())
ram_memory = int(input())

video_cards_price = video_cards * 250
procesors_price = (video_cards_price * (35 / 100)) * procesors
ram_memory_price = (video_cards_price / 10) * ram_memory
total_price = video_cards_price + procesors_price + ram_memory_price

if video_cards > procesors:
    total_price -= total_price * (15 / 100)

if budget >= total_price:
    print(f'You have {budget - total_price:.2f} leva left!')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva more!')