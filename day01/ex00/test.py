from book import Book
from recipe import Recipe

tourte = Recipe('tourte', 5, 10, ['asd', 'egg'], 'Une tourte.', 'starter')
print(tourte)

book = Book('Livre')
book.add_recipe(tourte)
print(book.get_recipe_by_name('tourte'))
print(book.get_recipes_by_types('starter'))
