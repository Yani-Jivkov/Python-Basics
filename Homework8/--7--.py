n = int(input())
total_people = 0
musala_people = 0
monblan_people = 0
kilimandwaro_people = 0
k2_people = 0
everest_people = 0

for i in range(n):
    group_people = int(input())
    total_people += group_people
    if group_people <= 5:
        musala_people += group_people
    elif group_people <= 12:
        monblan_people += group_people
    elif group_people <= 25:
        kilimandwaro_people += group_people
    elif group_people <= 40:
        k2_people += group_people
    elif group_people >= 41:
        everest_people += group_people

musala_people_percent = musala_people / total_people * 100
monblan_people_percent = monblan_people / total_people * 100
kilimandwaro_people_percent = kilimandwaro_people / total_people * 100
k2_people_percent = k2_people / total_people * 100
everest_people_percent = everest_people / total_people * 100

print(f'{musala_people_percent:.2f}%')
print(f'{monblan_people_percent:.2f}%')
print(f'{kilimandwaro_people_percent:.2f}%')
print(f'{k2_people_percent:.2f}%')
print(f'{everest_people_percent:.2f}%')