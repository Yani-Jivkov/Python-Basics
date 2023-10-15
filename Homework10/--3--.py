eks_money = float(input())
money = float(input())
spend_func = 0
days_saved = 0
save_func = 0

while money < eks_money and spend_func < 5:
    function = input()
    function_money = float(input())
    days_saved += 1

    if function == 'spend':
        spend_func += 1
        money -= function_money
        if money <= 0:
            money = 0
    elif function == 'save':
        money += function_money
        spend_func = 0
        if money >= eks_money:
            print(f'You saved the money for {days_saved} days.')
            break

    if spend_func >= 5:
        print("You can't save the money.")
        print(days_saved)
        break