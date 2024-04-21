
""" define the list of upcoming birthdays in 7 days"""


from datetime import datetime, timedelta, date


today = datetime.today().date()

def get_upcoming_birthdays(users: list) -> list:
    upcoming_birthdays = []
    for user in users:
        birth_date = datetime.strptime(user['birthday'], "%Y.%m.%d").date()
        birthday_this_year = date(today.year, birth_date.month, birth_date.day)        
        
        if birthday_this_year < today:
            birthday_this_year = date(today.year+1, birth_date.month, birth_date.day)
        
        birthday_weekday = birthday_this_year.isoweekday()
        if birthday_weekday == 6:
            birthday_this_year += timedelta(days=2)                
        elif birthday_this_year == 7:
            birthday_this_year += timedelta(days=1)

        if (birthday_this_year - today).days >= 0 and (birthday_this_year - today).days <= 7:
            upcoming_birthdays.append({'name': user.get('name'), 
                                       'congratulation_date': birthday_this_year.strftime("%Y.%m.%d")})
    return upcoming_birthdays


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)