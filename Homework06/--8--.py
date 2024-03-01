exam_hour = int(input())
exam_minutes = int(input())
araving_hour = int(input())
araving_minutes = int(input())

if exam_hour < araving_hour and exam_minutes < araving_minutes:
    late_hour = exam_hour - araving_hour
    late_minutes = exam_minutes < araving_minutes
    print('Late')
    print(f'{abs(late_hour)}:{abs(late_minutes)} hours after the start')
elif exam_hour == araving_hour and exam_minutes < araving_minutes:
    late_minutes = exam_minutes - araving_minutes
    print('Late')
    print(f'{abs(late_minutes)} minutes after the start')
elif exam_hour == araving_hour and exam_minutes > araving_minutes:
    on_start_minutes = abs(araving_minutes - exam_minutes)
    if 30 > on_start_minutes:
        print('Early')
        print(f'{abs(on_start_minutes)} minutes before the start')
    else:
        print('On time')
        print(f'{abs(on_start_minutes)} minutes before the start')
elif exam_hour > araving_hour and exam_minutes > araving_minutes:
    early_hour = exam_hour - araving_hour
    early_minutes = exam_minutes < araving_minutes
    print('Early')
    print(f'{abs(early_hour)}:{abs(early_minutes)} hours after the start')
