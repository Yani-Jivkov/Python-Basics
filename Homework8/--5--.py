n = int(input())
salary = int(input())
cost = 0

for i in range(n):
    site = input()
    if site == 'Facebook':
        cost += 150
    elif site == 'Instagram':
        cost += 100
    elif site == 'Reddit':
        cost += 50

if salary <= cost:
    print('You have lost your salary.')
else:
    print(salary - cost)