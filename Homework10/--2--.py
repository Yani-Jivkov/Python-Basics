max_bad_grades = int(input())
all_ex = 0
bad_grades = 0
total = 0

while True:
    ex_name = input()

    if ex_name == 'Enough':
        print(f'Average score: {average:.2f}')
        print(f'Number of problems: {all_ex}')
        print(f'Last problem: {last_ex}')
        break

    grade = int(input())
    last_ex = ex_name


    if grade <= 4:
        bad_grades += 1
        if bad_grades >= max_bad_grades:
            print(f'You need a break, {bad_grades} poor grades.')
            break

    all_ex += 1
    total += grade
    average = total / all_ex

