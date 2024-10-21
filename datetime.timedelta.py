from calendar import firstweekday
from datetime import date, datetime, timedelta

first_date = datetime.strptime(input(), '%d.%m.%Y')
last_date = datetime.strptime(input(), '%d.%m.%Y')
while (first_date.day + first_date.month) % 2 == 0:
    first_date += timedelta(days=1)
else:
    first_date = first_date
while first_date <= last_date:
    if str(first_date.weekday()) in '12456':
        print(date.strftime(first_date, '%d.%m.%Y'))
    first_date += timedelta(days=3)







