class Date:
    def is_date(day, month, year):
        return day == month

class isDate(Date):
    def increment_month(day, month, year):
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        return day, month, year

day = 10
month = 10
year = 2023

if Date.is_date(day, month, year):
    print("Номер месяца и день совпадает")

next_month_day, next_month, next_year = isDate.increment_month(day, month, year)
print(f"Следующий месяц: {next_month}.{next_year}")
