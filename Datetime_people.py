from datetime import datetime, timedelta

def choose_plural(amount, choose_plural):
    if amount % 10 == 0 or amount % 100 == 11 or amount % 100 == 12 or amount % 5 == 0 or amount % 10 == 6 or amount % 10 == 7 or amount % 10 == 8 or amount % 10 == 9:
        return f"{amount} {choose_plural[2]}"
    elif amount % 10 == 1:
        return f"{amount} {choose_plural[0]}"
    else:
        return f"{amount} {choose_plural[1]}"

today = datetime.strptime(input(), '%d.%m.%Y %H:%M')
plan = datetime(2022, 11, 8, 12, 00)
print(plan)
print((plan - today).minutes)
#08.11.2022 11:40
