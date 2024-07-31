from data import Data
from praktikum.bun import Bun


class TestBun:
    # Создание объекта bun с заданным именем. Проверка, соответствия возвращаемого значения с ожидаемым именем
    def test_get_name_correct_name_exist(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_name() == Data.BUN_NAME

    # Создание объекта bun с заданной ценой. Проверка, соответствия возвращаемого значения с ожидаемой ценой
    def test_get_price_correct_price_exist(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_price() == Data.BUN_PRICE
