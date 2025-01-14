import datetime as dt

# creating bday function


def get_days_to_birthday(date_birthday):
    today = dt.date.today()
    today_year = today.year
    date_birthday = date_birthday.replace(year=today_year)
    if today > date_birthday:
        date_birthday = date_birthday.replace(year=today_year+1)
    day_counter = date_birthday - today
    return day_counter.days


# establish today date
# today = dt.date.today()
# print(today)

# establish kids bdays
lera_bday = dt.date(year=2015, month=1, day=13)
print(lera_bday)
max_bday = dt.date(year=2011, month=12, day=16)
print(max_bday)

# establish today year
# today_year = today.year
# print(today_year)

# replace kids bdays years on current
# lera_bday = lera_bday.replace(year=today_year)
# print(lera_bday)
# max_bday = max_bday.replace(year=today_year)
# print(max_bday)

# find difference from today till bdays
# till_lera_bday = lera_bday - today
# print(till_lera_bday.days)
# till_max_bday = max_bday - today
# print(till_max_bday.days)

print(get_days_to_birthday(lera_bday))
print(get_days_to_birthday(max_bday))