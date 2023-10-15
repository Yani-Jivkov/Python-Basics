cena_ekskurziq = float(input())
broi_puzeli = int(input())
broi_kukli = int(input())
broi_mecheta = int(input())
broi_minioni = int(input())
broi_kamioncheta = int(input())
cena_puzeli = broi_puzeli * 2.6
cena_kukli = broi_kukli * 3
cena_mecheta = broi_mecheta * 4.1
cena_minion = broi_minioni * 8.2
cena_kamioncheta = broi_kamioncheta * 2
total_broi = broi_puzeli \
             + broi_kukli \
             + broi_mecheta \
             + broi_kamioncheta \
             + broi_minioni

total_sum = cena_puzeli \
            + cena_kukli \
            + cena_mecheta \
            + cena_minion \
            + cena_kamioncheta


if total_broi > 50:
    total_sum = total_sum - (total_sum / 4)
    total_sum = total_sum - (total_sum / 10)
else:
    total_sum = total_sum - (total_sum / 10)


if total_sum > cena_ekskurziq:
    print(f'Yes! {total_sum - cena_ekskurziq:.2f} lv left.')
else:
    print(f'Not enough money! {cena_ekskurziq - total_sum:.2f} lv needed.')
