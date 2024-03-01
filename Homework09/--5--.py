total = 0

while True:
    text = input()

    if text == 'NoMoreMoney':
        break

    inc_num = float(text)

    if inc_num >= 0:
        total += inc_num
        print(f'Increase: {inc_num:.2f}')
    else:
        print('Invalid operation!')
        break
print(f'Total: {total:.2f}')