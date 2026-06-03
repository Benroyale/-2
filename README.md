# Recipe Manager

Консольное приложение для управления рецептами. Позволяет создавать блюда, добавлять ингредиенты, масштабировать порции и автоматически составлять список покупок.

## Установка

```bash
git clone https://github.com/Benroyale/-2.git
cd МанашеровБэнТПдз2
pip install -r requirements.txt
```

## Использование

Все классы находятся в файле `recipes.py`. Чтобы использовать их в своём коде — импортируй:

```python
from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe
```

Запуск тестов:

```bash
pytest
```

## Структура проекта

- `recipes.py` — основные классы: Ingredient, Recipe, ShoppingList, DietaryRecipe
- `test_recipes.py` — тесты
- `requirements.txt` — зависимости

## Автор

Манашеров Бэн Семенович, группа ББИ2505, НИУ ВШЭ, 2025-26