class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit


    @property
    def quantity(self):
        return self._quantity


    @quantity.setter
    def quantity(self, value):
        if value <= 0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = float(value)


    def __str__(self):
        return (f'{self.name}: {self.quantity} {self.unit}')


    def __repr__(self):
        return f"Ingredient('{self.name}', {self.quantity}, '{self.unit}')"


    def __eq__(self, other):
        return self.name == other.name and self.unit == other.unit


class Recipe:
    def __init__(self, title, ingredients=None):
        self.title = title
        if ingredients is not None:
            self.ingredients = ingredients
        else:
            self.ingredients = []

    def add_ingredient(self, ingredient: Ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        if isinstance(ratio, (int, float)) and ratio > 0:
            return True
        return False


    def scale(self, ratio: float):
        if not(Recipe.is_valid_ratio(ratio)):
            raise ValueError
        new_recipe = Recipe(self.title)
        for i in self.ingredients:
            new_ingredient = Ingredient(i.name, i.quantity * ratio, i.unit)
            new_recipe.add_ingredient(new_ingredient)
        return new_recipe


    def __len__(self):
        return len(self.ingredients)


    def __str__(self):
        result = f"{self.title}:\n"
        for i in self.ingredients:
            result += f"  {i}\n"
        return result


