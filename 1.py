def is_date(day, month, year):
    return day == month
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

if is_date(day, month, year):
    print("Nomer mesyaca i den sovpadaet")

next_month_day, next_month, next_year = increment_month(day, month, year)
print(f"Sled mesyac: {next_month}.{next_year}")