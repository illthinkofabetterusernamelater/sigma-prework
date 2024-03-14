from datetime import datetime

today = datetime.now()

def take_input(period):
    dict = {'day': 31, 'month': 12, 'year': today.year }
    while True:
        time = int(input(f'Enter a {period}: '))
        if time > dict[period]:
            print(f'Error please enter a valid {period}')
        else:
            return time

age = 0

day1 = take_input('day')
month1 = take_input('month')
year1 = take_input('year')

if today.month > month1:
    age = today.year - year1
elif today.month <= month1:
    if today.day >= day1:
        age = today.year - year1 - 1
    else:
        age = today.year - year1 - 1

print(age)


