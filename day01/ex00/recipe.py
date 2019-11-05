
class Recipe():
    """A recipe in the cookbook"""

    def __init__(self, name, cooking_lvl, cooking_time,
            ingredients, description, recipe_type):

        if type(name) is not str:
            raise ValueError("name is not a string")
        if type(cooking_lvl) is not int or cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("cooking level is not an integer in range 1-5")
        if type(cooking_time) is not int or cooking_time < 0:
            raise ValueError("cooking time is not a positive integer")
        if type(ingredients) is not list or \
                any(type(i) is not str for i in ingredients):
            raise ValueError("ingredients is not a list of strings")
        if type(description) is not str:
            raise ValueError("description is not a string")
        if recipe_type not in ['starter', 'lunch', 'dessert']:
            raise ValueError("recipe type should be one of starter, " +
                    "lunch, dessert")

        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type


    def __str__(self):
        """Return the string to print with the recipe info"""

        return '{}: {} ({}min, {}) [level {}] [{}]'.format(
                self.name, self.description, self.cooking_time,
                self.recipe_type, self.cooking_lvl,
                ', '.join(self.ingredients))

