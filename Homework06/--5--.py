budget = float(input())
season = input()

if 100 >= budget:
    destination = 'Bulgaria'
    if season == 'summer':
        budget *= 0.3
        relax = 'Camp'
    elif season == 'winter':
        budget *= 0.7
        relax = 'Hotel'
elif 1000 >= budget:
    destination = 'Balkans'
    if season == 'summer':
        budget *= 0.4
        relax = 'Camp'
    elif season == 'winter':
        budget *= 0.8
        relax = 'Hotel'
elif 1000 < budget:
    destination = 'Europe'
    budget *= 0.9

if destination == 'Europe':
    print(f'Somewhere in {destination}')
    print(f'Hotel - {budget:.2f}')
else:
    print(f'Somewhere in {destination}')
    print(f'{relax} - {budget:.2f}')