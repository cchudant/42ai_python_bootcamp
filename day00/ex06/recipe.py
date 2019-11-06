cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10,
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60,
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15,
    },
}


def show_recipe(name):
    r = cookbook[name]

    print('Recipe for {}:'.format(name))
    print('Ingredients list:', r['ingredients'])
    print('To be eaten for {}.'.format(r['meal']))
    print('Takes {} minutes of cooking.'.format(r['prep_time']))


def del_recipe(name):
    del cookbook[name]


def add_recipe(name, ingredients, meal, prep_time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time,
    }


def show_cookbook():
    print('All recipes:')
    for name, r in cookbook.items():
        print('{} ({}min - {})'.format(name, r['prep_time'], r['meal']))


choice = None
while choice != '5':
    print('Please select an option by typing the corresponding number:')
    print('1: Add a recipe')
    print('2: Delete a recipe')
    print('3: Print a recipe')
    print('4: Print the cookbook')
    print('5: Quit')

    choice = input('>> ')
    if choice == '1':
        print('Please enter the name of your recipe:')
        name = input('>> ')
        print('Please enter the type of meal:')
        meal = input('>> ')
        print('Please enter the preparation time:')
        prep_time = ''
        while not prep_time.isdigit():
            prep_time = input('>> ')
            if not prep_time.isdigit():
                print('This value is not a valid preparation time.')
        ingredients = []
        ingr = None
        print('Please enter the arguments (send nothing to end the list):')
        while ingr != '':
            ingr = input('>> ')
            if ingr != '':
                ingredients.append(ingr)
        add_recipe(name, ingredients, meal, prep_time)
        print('Recipe added!')
    elif choice == '2':
        print('Please enter the recipe\'s name to remove it:')
        name = input('>> ')
        if name not in cookbook:
            print('This recipe is not in the cookbook!')
        else:
            del_recipe(name)
            print('Removed!')
    elif choice == '3':
        print('Please enter the recipe\'s name to get its details:')
        name = input('>> ')
        if name not in cookbook:
            print('This recipe is not in the cookbook!')
        else:
            show_recipe(name)
    elif choice == '4':
        show_cookbook()
