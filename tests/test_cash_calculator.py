import sys
sys.path.append('..')

from Seminars_project.laboratory import Record, CashCalculator


def test_get_today_cash_remained():
    """Тестируем калькулятор трат"""
    cash_calculator = CashCalculator(1500)  # init calculator
    records = [Record(amount=110, comment="кофе с утра"),
               Record(amount=350, comment="Обед в столовке"),
               Record(amount=3000, comment="бар в Танин др", date="08.01.2022")]  # create records

    for record in records:
        cash_calculator.add_record(record)  # insert records in calculator

    """test right away get today limit balance as it already contain get_today_stats"""
    assert cash_calculator.get_today_limit_balance() == 1500 - (records[0].amount + records[1].amount)


def test_get_week_stats():

    cash_calculator = CashCalculator(1500)  # init calculator

    records = [Record(amount=110, comment="кофе с утра"),
               Record(amount=350, comment="Обед в столовке", date="21.02.2022"),
               Record(amount=350, comment="Обед в столовке", date="19.02.2022"),
               Record(amount=350, comment="Обед в столовке", date="20.02.2022"),
               Record(amount=3000, comment="бар в Танин др", date="10.02.2022")]

    for record in records:
        cash_calculator.add_record(record)  # insert records in calculator

    amounts = records[0].amount + records[1].amount + records[2].amount + records[3].amount  # sum valid records

    """test get week stats as the amount of week expenses"""
    assert cash_calculator.get_week_stats() == amounts
