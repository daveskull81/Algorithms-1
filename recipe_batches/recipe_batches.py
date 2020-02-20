#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  for key in recipe:
    if key in ingredients:
      if ingredients[key] - recipe[key] >= 0:
        # Subtract the recipe amount from the ingredients list
        ingredients[key] = ingredients[key] - recipe[key]
      else:
        return 0
    else:
      return 0
  
  return 1 + recipe_batches(recipe, ingredients)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))