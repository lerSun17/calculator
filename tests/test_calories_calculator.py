import sys
sys.path.append('..')

from Seminars_project.laboratory import Record, CaloriesCalculator


def test_get_calories_remained():
    """Тестируем калькулятор калорий."""

    calories_calculator = CaloriesCalculator(1500)  # init calc
    records = [Record(amount=110, comment=",булочка"),
               Record(amount=350, comment="удон с курицей"),
               Record(amount=350, comment="удон с курицей"),
               Record(amount=350, comment="фобо"),
               Record(amount=3000, comment="пицца и суши", date="08.01.2022")]  # create records

    for record in records:
        calories_calculator.add_record(record)  # insert records

    amounts = records[0].amount + records[1].amount + records[2].amount + records[3].amount  # sum valid records

    """test right away get today limit balance as it already contain get_today_stats"""
    assert calories_calculator.get_today_limit_balance() == 1500 - amounts


def test_get_week_stats():

    cash_calculator = CaloriesCalculator(1500)  # init calculator

    records = [Record(amount=110, comment="булочка"),
               Record(amount=350, comment="суп", date="21.02.2022"),
               Record(amount=350, comment="курица запеченая", date="19.02.2022"),
               Record(amount=350, comment="гречка с салатом", date="20.02.2022"),
               Record(amount=3000, comment="пицца и суши", date="10.02.2022")]

    for record in records:
        cash_calculator.add_record(record)  # insert records in calculator

    amounts = records[0].amount + records[1].amount + records[2].amount + records[3].amount  # sum valid records

    """test get week stats as the amount of week expenses"""
    assert cash_calculator.get_week_stats() == amounts


