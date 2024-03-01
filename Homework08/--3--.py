n = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for i in range(0, n):
    num = int(input())
    if num < 200:
        p1_count += 1
    elif num <= 399:
        p2_count += 1
    elif num <= 599:
        p3_count += 1
    elif num <= 799:
        p4_count += 1
    elif num >= 800:
        p5_count += 1

p1 = p1_count / n * 100
p2 = p2_count / n * 100
p3 = p3_count / n * 100
p4 = p4_count / n * 100
p5 = p5_count / n * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')

