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


class ShoppingList:
    def __init__(self, _items=None):
        if _items is None:
            self._items = []
        else:
            self._items = _items


    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительно")
        new_recipe = recipe.scale(portions)
        for e in new_recipe.ingredients:
            self._items.append((e, recipe.title))


    def remove_recipe(self, title: str):
        self._items = [x for x in self._items if x[1] != title]


    def get_list(self):
        sp = {}
        for e in self._items:
            nam = e[0].name
            ingr = e[0].unit
            if (nam, ingr) not in sp:
                sp[(nam, ingr)] = e[0].quantity
            else:
                sp[(nam, ingr)] += e[0].quantity
        new_sp = []
        for e in sp:
            new_Ingredient = Ingredient(e[0], sp[e], e[1])
            new_sp.append(new_Ingredient)
        new_sp.sort(key=lambda x: x.name)
        return new_sp

    def __add__(self, other: ShoppingList):
        new_list = ShoppingList()
        new_list._items = self._items + other._items
        return new_list


class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        self.diet_type = diet_type
        super().__init__(title, ingredients)


    def scale(self, ratio: float):
        scal = super().scale(ratio)
        return DietaryRecipe(scal.title, self.diet_type, scal.ingredients)


    def __str__(self):
        return f'[{self.diet_type}] {super().__str__()}'