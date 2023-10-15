from math import floor

n = int(input())
starter_point = int(input())
w_points = 0
wins = 0
f_points = 0
sf_points = 0

for i in range(n):
    place = input()
    if place == 'W':
        w_points += 2000
        wins += 1
    elif place == 'F':
        f_points += 1200
    elif place == 'SF':
        sf_points += 720

total = w_points + f_points + sf_points + starter_point
average = (w_points + f_points + sf_points) / n
percent = (wins / n) * 100

print(f'Final points: {floor(total)}')
print(f'Average points: {floor(average)}')
print(f'{percent:.2f}%')