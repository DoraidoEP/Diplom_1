import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import Data


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.name = Data.INGREDIENT_SAUCE_NAME
    mock_ingredient_sauce.price = Data.INGREDIENT_SAUCE_PRICE
    mock_ingredient_sauce.type = Data.INGREDIENT_SAUCE_TYPE
    mock_ingredient_filling = Mock()
    mock_ingredient_filling.name = Data.INGREDIENT_FILLING_NAME
    mock_ingredient_filling.price = Data.INGREDIENT_FILLING_PRICE
    mock_ingredient_filling.type = Data.INGREDIENT_FILLING_TYPE
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = Data.BUN_NAME
    mock_bun.price = Data.BUN_PRICE
    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient_sauce():
    mock_ingredient_sauce = Mock()
    mock_ingredient_sauce.name = Data.INGREDIENT_SAUCE_NAME
    mock_ingredient_sauce.price = Data.INGREDIENT_SAUCE_PRICE
    mock_ingredient_sauce.type = Data.INGREDIENT_SAUCE_TYPE
    return mock_ingredient_sauce


@pytest.fixture(scope='function')
def mock_ingredient_filling():
    mock_ingredient_filling = Mock()
    mock_ingredient_filling.name = Data.INGREDIENT_FILLING_NAME
    mock_ingredient_filling.price = Data.INGREDIENT_FILLING_PRICE
    mock_ingredient_filling.type = Data.INGREDIENT_FILLING_TYPE
    return mock_ingredient_filling

