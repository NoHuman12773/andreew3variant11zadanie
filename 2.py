from datetime import date


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


class Medicine(Date):
    def __init__(self, name, day, month, year, company):
        super().__init__(day, month, year)
        self.name = name
        self.company = company

    def days_since(self):
        today = date.today()
        manufacture_date = date(self.year, self.month, self.day)
        delta = today - manufacture_date
        return delta.days


med = Medicine("Аспирин", 1, 1, 2022, "Таблетка")
days_since = med.days_since()
print(f"Прошло {days_since} дней со дня изготовления лекарства {med.name} от {med.company}")