total = 0
target_steps = 10000

while total < target_steps:
    text = input()

    if text == 'Going home':
        to_home = int(input())
        total += to_home
        if target_steps <= total:
            print(f'Goal reached! Good job!')
            print(f'{total - target_steps} steps over the goal!')
            break
        else:
            print(f'{target_steps - total} more steps to reach goal.')
            break

    steps_today = int(text)
    total += steps_today

    if target_steps <= total:
        print(f'Goal reached! Good job!')
        print(f'{total - target_steps} steps over the goal!')
        break
else:
    print(f'{target_steps - total} more steps to reach goal.')