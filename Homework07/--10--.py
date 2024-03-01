n = int(input())
odd_total = 0
even_total = 0

for i in range(n):
    number = int(input())
    if i % 2 == 0:
        even_total += number
    else:
        odd_total += number

if even_total == odd_total:
    print('Yes')
    print(f'Sum = {even_total}')
elif even_total > odd_total:
    print('No')
    print(f'Diff = {abs(even_total - odd_total)}')
elif even_total < odd_total:
    print('No')
    print(f'Diff = {abs(odd_total - even_total)}')
