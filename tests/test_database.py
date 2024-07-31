from data import Data
from praktikum.database import Database


class TestDatabase:
    # Cоздание экземпляра класса Database
    # Вызов метода available_buns(), который возвращает список доступных булочек
    # Проверка, что имя первой булочки в списке метода available_buns(), соответствует ожидаемому значению
    def test_available_buns_successfully(self):
        data = Database()
        buns = data.available_buns()
        assert buns[0].name == Data.BUN_NAME

    # Cоздание экземпляра класса Database
    # Вызов метода available_ingredients(), который возвращает список доступных ингредиентов
    # Проверка, что имя первого ингредиента в списке метода available_ingredients(), соответствует ожидаемому значению
    def test_available_ingredients_successfully(self):
        data = Database()
        ingredients = data.available_ingredients()
        assert ingredients[0].name == Data.INGREDIENT_SAUCE_NAME
