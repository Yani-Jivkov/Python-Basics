from math import floor

record = float(input())
raztoqnie_m = float(input())
vreme_za_1m = float(input())
total_time = raztoqnie_m * vreme_za_1m
total_time = total_time + ((raztoqnie_m // 15) * 12.5)

if record > total_time:
    print(f'Yes, he succeeded! The new world record is {floor(total_time):.2f} seconds.')
else:
    print(f'No, he failed! He was {floor(total_time - record):.2f} seconds slower.')
