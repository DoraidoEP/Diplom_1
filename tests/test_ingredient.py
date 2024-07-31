from praktikum.ingredient import Ingredient
from data import Data


class TestIngredient:
    # Создание объекта ingredient с заданными параметрами.
    # Проверка, соответствия возвращаемого значения метода get_price() ожидаемой цене.
    def test_get_price_correct_price_exist(self):
        ingredient = Ingredient(Data.INGREDIENT_SAUCE_TYPE, Data.INGREDIENT_SAUCE_NAME, Data.INGREDIENT_SAUCE_PRICE)
        assert ingredient.get_price() == Data.INGREDIENT_SAUCE_PRICE

    # Создание объекта ingredient с заданными параметрами.
    # Проверка, соответствия возвращаемого значения метода get_name() ожидаемому имени.
    def test_get_name_correct_name_exist(self):
        ingredient = Ingredient(Data.INGREDIENT_SAUCE_TYPE, Data.INGREDIENT_SAUCE_NAME, Data.INGREDIENT_SAUCE_PRICE)
        assert ingredient.get_name() == Data.INGREDIENT_SAUCE_NAME

    # Создание объекта ingredient с заданными параметрами.
    # Проверка, соответствия возвращаемого значения метода get_type() ожидаемому типу.
    def test_get_type_correct_type_exist(self):
        ingredient = Ingredient(Data.INGREDIENT_SAUCE_TYPE, Data.INGREDIENT_SAUCE_NAME, Data.INGREDIENT_SAUCE_PRICE)
        assert ingredient.get_type() == Data.INGREDIENT_SAUCE_TYPE

