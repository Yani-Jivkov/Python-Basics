from math import ceil

name_of_film = str(input())
time_of_film = int(input())
time_break = int(input())

otdih = time_break * 1/8
obqd = time_break * 1/4
time_break -= (otdih + obqd)

if time_of_film < time_break:
    print(f'You have enough time to watch {name_of_film} and left with {ceil(time_break - time_of_film)} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {name_of_film}, you need {ceil(time_of_film - time_break)} more minutes.')