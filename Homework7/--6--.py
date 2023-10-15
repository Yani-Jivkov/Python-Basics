tekst = input()
glasni_stoinosti = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
suma = 0

for bukva in tekst:
    if bukva in glasni_stoinosti:
        suma += glasni_stoinosti[bukva]

print(f'{suma}')
