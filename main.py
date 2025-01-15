import datetime as dt
FORMAT = '%d.%m.%Y'
lera_bday = dt.date(year=2015, month=5, day=16)
max_bday = dt.date(year=2011, month=12, day=16)
birthdays = [
    ('Лера', '16.05.2015'),
    ('Максим', '16.12.2011'),
    ('Толя', '12.06.2016')
]
# creating bday function


def get_days_to_birthday(name, date_birthday):
    date_birthday = dt.datetime.strptime(date_birthday, FORMAT)
    today = dt.datetime.today()
    date_birthday = date_birthday.replace(year=today.year)
    if today > date_birthday:
        date_birthday = date_birthday.replace(year=today+1)
    day_counter = date_birthday - today
    return f'{name}, до твоего дня рождения осталось дней: {day_counter.days}'


for bday in birthdays:
    print(get_days_to_birthday(bday[0], bday[1]))