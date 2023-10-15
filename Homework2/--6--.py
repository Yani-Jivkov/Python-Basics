nailon = int(input()) + 2
boq = int(input())
razreditel = int(input())
workers_time = int(input())
boq = boq + (boq / 10)
cena_nailon = nailon * 1.50
cena_boq = boq * 14.50
cena_razreditel = razreditel * 5
total_materials = cena_boq + cena_nailon + cena_razreditel + 0.4
cena_workers = workers_time * (total_materials * (30 / 100))
total_sum = total_materials + cena_workers

print(total_sum)