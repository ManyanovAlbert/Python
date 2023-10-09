M = int(input())
fridge_products = set(input().split())
N = int(input())

recipes_to_cook = []
for _ in range(N):
    recipe_name = input() 
    num_ingredients = int(input()) 
    ingredients = set(input().split()) 
    if ingredients.issubset(fridge_products):
        recipes_to_cook.append(recipe_name)
for recipe in recipes_to_cook:
    print(recipe)