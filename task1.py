from datetime import datetime

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y-%m-%d")

def get_days_from_today(date):
    try:
        date_date = string_to_date(date)
        today = datetime.today()
        return (today - date_date).days
    except ValueError:
        print("Не вірний формат дати")

print(get_days_from_today("2024-09-01"))