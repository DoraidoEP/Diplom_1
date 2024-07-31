from conftest import burger, mock_bun, mock_ingredient_sauce, mock_ingredient_filling
from praktikum.burger import Burger


class TestBurger:
    def test_set_buns_correct_bun_exist(self, mock_bun):
        # Создаем новый объект Burger
        burger = Burger()
        # Устанавливаем булочку (mock_bun) с помощью метода set_buns
        burger.set_buns(mock_bun)
        # Проверяем, что установленная булочка соответствует переданному mock_bun
        assert burger.bun == mock_bun

    def test_add_ingredient_correct_ingredient_exist(self, mock_ingredient_sauce):
        # Создаем новый объект Burger
        burger = Burger()
        # Добавляем ингредиент (mock_ingredient_sauce) с помощью метода add_ingredient
        burger.add_ingredient(mock_ingredient_sauce)
        # Проверяем, что добавленный ингредиент присутствует в списке ингредиентов бургера
        assert mock_ingredient_sauce in burger.ingredients

    def test_remove_ingredient_correct_ingredient_not_exist(self, mock_ingredient_sauce):
        # Создаем новый объект Burger
        burger = Burger()
        # Добавляем ингредиент (mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_sauce)
        # Находим индекс добавленного ингредиента и удаляем его с помощью метода remove_ingredient
        index = burger.ingredients.index(mock_ingredient_sauce)
        burger.remove_ingredient(index)
        # Проверяем, что удаленный ингредиент больше не присутствует в списке ингредиентов
        assert mock_ingredient_sauce not in burger.ingredients

    def test_move_ingredient_correct_ingredient_new_index(self, burger):
        # Используем существующий объект burger, который уже содержит ингредиенты
        # Сохраняем первый ингредиент в переменную
        ingredient = burger.ingredients[0]
        # Перемещаем первый ингредиент на вторую позицию с помощью метода move_ingredient
        burger.move_ingredient(1, 0)
        # Проверяем, что ингредиент на новой позиции соответствует ранее сохраненному ингредиенту
        assert burger.ingredients[1] == ingredient

    def test_get_price_correct_price(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        # Создаем новый объект Burger
        burger = Burger()
        # Добавляем два ингредиента (mock_ingredient_sauce и mock_ingredient_filling)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        # Устанавливаем булочку (mock_bun)
        burger.set_buns(mock_bun)
        # Настраиваем цены для булочки и ингредиентов через mock-объекты
        mock_bun.get_price.return_value = 100
        mock_ingredient_sauce.get_price.return_value = 100
        mock_ingredient_filling.get_price.return_value = 100
        # Проверяем, что общая цена бургера соответствует ожидаемой сумме (400)
        assert burger.get_price() == 400

    def test_get_receipt_correct_receipt(self, mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
        # Создаем новый объект Burger
        burger = Burger()
        # Устанавливаем булочку и добавляет два ингредиента
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_sauce)
        burger.add_ingredient(mock_ingredient_filling)
        # Настраиваем имена и цены для булочки и ингредиентов через mock-объекты
        mock_bun.get_name.return_value = 'black bun'
        mock_bun.get_price.return_value = 100
        mock_ingredient_sauce.get_name.return_value = 'hot sauce'
        mock_ingredient_sauce.get_price.return_value = 100
        mock_ingredient_sauce.get_type.return_value = 'hot sauce'
        mock_ingredient_filling.get_name.return_value = 'cutlet'
        mock_ingredient_filling.get_price.return_value = 100
        mock_ingredient_filling.get_type.return_value = 'cutlet'
        # Формируем ожидаемый чек (receipt) в виде списка строк
        receipt = [
            '(==== black bun ====)',
            '= hot sauce hot sauce =',
            '= cutlet cutlet =',
            '(==== black bun ====)\n',
            'Price: 400'
        ]
        # Проверяем, что возвращаемая строка из метода get_receipt соответствует ожидаемому чеку
        assert '\n'.join(receipt) == burger.get_receipt()

