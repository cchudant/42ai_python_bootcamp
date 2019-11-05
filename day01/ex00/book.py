from datetime import datetime

class Book():
    """The cookbook"""

    def __init__(self, name):

        if type(name) is not str:
            raise ValueError('name is not a string')

        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = { 'lunch': {}, 'starter': {}, 'dessert': {} }

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""

        recipe = next((d[name] for d in self.recipes_list.values()
                if name in d), None)
        if recipe == None:
            raise ValueError('name is not in recipes_list')

        return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type"""

        return list(self.recipes_list[recipe_type].values())

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""

        self.last_update = datetime.now()
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe
