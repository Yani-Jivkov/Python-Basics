name = input()
total = 0
bad = 0
clas = 0

while True:
    grade = float(input())
    if grade >= 4:
        total += grade
    else:
        bad += 1

        if bad >= 2:
            print(f'{name} has been excluded at {clas + 1} grade')
            break

        continue
    clas += 1

    if clas == 12:
        break

if bad != 2:
    average = total / 12
    print(f"{name} graduated. Average grade: {average:.2f}")