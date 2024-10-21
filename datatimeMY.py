from datetime import datetime, timedelta

pattern = '%d.%m.%Y %H:%M'

now = datetime.strptime(input(), pattern)
time_now = timedelta(hours=now.hour, minutes=now.minute)
work_time = (timedelta(hours=9), timedelta(hours=21)) if now.weekday() in range(5) else (timedelta(hours=10), timedelta(hours=18))
if time_now >= work_time[1] or time_now < work_time[0]:
    print('Магазин не работает')
else:
    a = (work_time[1] - time_now)
    b = a.seconds / 60
    print(int(b))

