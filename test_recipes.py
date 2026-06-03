import pytest
from recipes import *
def test_base1():
    i1 = Ingredient('Мука', 500, 'г')
    assert i1.name == 'Мука'
    assert i1.quantity == 500
    assert i1.unit == 'г'


def test_negative_ingredient():
    with pytest.raises(ValueError):
        Ingredient('Мука', -100,'г')


def test__str__():
    i1 = Ingredient('Мука', 500, 'г')
    assert str(i1) == "Мука: 500.0 г"


def test__eq__():
    i1 = Ingredient('Мука', 500, 'г')
    i2 = Ingredient('Мука', 300, 'г')
    i3 = Ingredient('Соль', 500, 'г')
    i4 = Ingredient('Мука', 500, 'кг')
    assert i1 == i2
    assert i1 != i3
    assert i1 != i4


def test_base2():
    flour = Ingredient("Мука", 500, "г")
    salt = Ingredient("Соль", 10, "г")
    recipe1 = Recipe('Пицца', [flour, salt])
    assert recipe1.title == 'Пицца'
    assert recipe1.ingredients == [flour, salt]

def test_add_ingredient():
    pizza = Recipe("Пицца")
    flour = Ingredient("Мука", 500, "г")
    flour2 = Ingredient("Мука", 200, "г")
    eggs = Ingredient("Яйца", 3, "шт")
    pizza.add_ingredient(flour)
    assert len(pizza) == 1
    pizza.add_ingredient(flour2)
    assert len(pizza) == 1
    assert pizza.ingredients[0].quantity == 700
    pizza.add_ingredient(eggs)
    assert len(pizza) == 2


def test_scale():
    pizza = Recipe("Пицца")
    pizza.add_ingredient(Ingredient("Мука", 500, "г"))
    scaled = pizza.scale(2)
    assert scaled is not pizza
    assert scaled.ingredients[0].quantity == 1000
    assert pizza.ingredients[0].quantity == 500
    with pytest.raises(ValueError):
        pizza.scale(-3)


def test_len():
    pizza = Recipe("Пицца")
    assert len(pizza) == 0

    pizza.add_ingredient(Ingredient("Мука", 500, "г"))
    assert len(pizza) == 1

    pizza.add_ingredient(Ingredient("Яйца", 3, "шт"))
    assert len(pizza) == 2


def test_add_recipe():
    pizza = Recipe("Пицца")
    pizza.add_ingredient(Ingredient("Мука", 500, "г"))
    shopping = ShoppingList()
    shopping.add_recipe(pizza, 2)
    assert len(shopping._items) == 1
    assert shopping._items[0][1] == "Пицца"
    assert shopping._items[0][0].quantity == 1000


def test_add_recipe_invalid_portions():
    pizza = Recipe("Пицца")
    shopping = ShoppingList()
    with pytest.raises(ValueError):
        shopping.add_recipe(pizza, 0)


def test_remove_recipe():
    pizza = Recipe("Пицца")
    pizza.add_ingredient(Ingredient("Мука", 500, "г"))
    pasta = Recipe("Паста")
    pasta.add_ingredient(Ingredient("Яйца", 3, "шт"))
    shopping = ShoppingList()
    shopping.add_recipe(pizza, 1)
    shopping.add_recipe(pasta, 1)
    shopping.remove_recipe("Пицца")
    assert len(shopping._items) == 1
    assert shopping._items[0][1] == "Паста"


def test_remove_recipe_not_found():
    shopping = ShoppingList()
    shopping.remove_recipe("Несуществующий")


def test_get_list():
    pizza = Recipe("Пицца")
    pizza.add_ingredient(Ingredient("Мука", 500, "г"))
    pasta = Recipe("Паста")
    pasta.add_ingredient(Ingredient("Мука", 300, "г"))
    shopping = ShoppingList()
    shopping.add_recipe(pizza, 1)
    shopping.add_recipe(pasta, 1)
    result = shopping.get_list()
    assert len(result) == 1
    assert result[0].quantity == 800
    assert result[0].name == "Мука"


def test_get_list_sorted():
    shopping = ShoppingList()
    recipe = Recipe("Тест")
    recipe.add_ingredient(Ingredient("Яйца", 3, "шт"))
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    recipe.add_ingredient(Ingredient("Соль", 10, "г"))
    shopping.add_recipe(recipe, 1)
    result = shopping.get_list()
    assert result[0].name == "Мука"
    assert result[1].name == "Соль"
    assert result[2].name == "Яйца"


def test_add_shopping_lists():
    pizza = Recipe("Пицца")
    pizza.add_ingredient(Ingredient("Мука", 500, "г"))
    pasta = Recipe("Паста")
    pasta.add_ingredient(Ingredient("Яйца", 3, "шт"))
    shop1 = ShoppingList()
    shop1.add_recipe(pizza, 1)
    shop2 = ShoppingList()
    shop2.add_recipe(pasta, 1)
    shop3 = shop1 + shop2
    assert len(shop3._items) == 2
    assert len(shop1._items) == 1
    assert len(shop2._items) == 1
