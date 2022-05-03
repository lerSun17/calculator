from datetime import datetime as dt
from datetime import timedelta
"""Import datetime libraries"""


class Record:

    def __init__(self, amount, comment, date=None):
        """define init there define common attrs, and set date it its none"""
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.today()
        else:
            self.date = dt.strptime(date, '%d.%m.%Y')


class Calculator:

    def __init__(self, limit):
        """define init with common attrs"""
        self.limit = limit
        self.records = []
        self.today = dt.today()
        self.week_ago = self.today - timedelta(7)

    def add_record(self, record):
        """method for record adding """
        self.records.append(record)

    def get_today_stats(self):
        """method for getting today stats as sum of valid records amount"""
        day_stats = 0
        for record in self.records:
            if record.date == self.today:
                day_stats += record.amount
        return day_stats

    def get_week_stats(self):
        """method for getting week stats as sum of valid records amount"""
        week_stats = 0
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats += record.amount
        return week_stats

    def get_today_limit_balance(self):
        """method for getting today balance over limit"""
        current_balance = self.limit - self.get_today_stats()
        return current_balance


class CashCalculator(Calculator):
    USD_RATE = 75.76
    EUR_RATE = 86.15
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE),
                      'eur': ('EURO', CashCalculator.EUR_RATE)}
        name, rate = currencies[currency]
        cash_remained = round(self.get_today_limit_balance() / rate, 2)
        if cash_remained == 0:
            print('You are broke!')
        elif cash_remained > 0:
            print(f'You still have {cash_remained} {name} for today')
        else:
            print(f'You are under-budget, your debt {abs(cash_remained)} {name}!')


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = self.get_today_limit_balance()
        if calories_remained > 0:
            print(f'You can eat something else, but keep it together, you only have {calories_remained} calories to left')
        else:
            print('Please, stop eating!!!')


cash_calculator = CashCalculator(1500)
cash_calculator.add_record(Record(amount=110, comment="кофе с утра"))
cash_calculator.add_record(Record(amount=350, comment="Обед в столовке"))
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
print(cash_calculator.get_today_cash_remained("rub"))
