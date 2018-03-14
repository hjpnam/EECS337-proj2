from Vocabulary import *
from Ingredient import Ingredient
from Recipe import Recipe
import copy
import nltk
from fractions import Fraction

def toVegetarian(recipe, vegOption):
	rec = recipe
	if vegOption.lower() not in vegetarian:
		return False
	animals = meat
	animals.extend(fish)
	steps = rec.directions
	food_list = rec.food_list
	serving = rec.serving
	
	for i in range(len(food_list)):
		for animal in animals:
			if animal in food_list[i].getName():	
				food_list[i].data['name'] = vegOption
				food_list[i].data['measurement'] = str(vegetarian_attribute[vegOption]['measurement'])
				food_list[i].data['quantity'] = str(vegetarian_attribute[vegOption]['servingSize']*serving)
				food_list[i].data['descriptor'] = 'none'
				food_list[i].data['preparation'] = 'none'
	
	for i in range(len(steps)):
		step_lower = steps[i].lower()
		for animal in animals:
			if animal in step_lower:
				step_lower = step_lower.replace(animal, vegOption)
				steps[i]=step_lower
	rec.food_list = food_list
	rec.directions = steps
	return rec

def MakeIndian(recipe):
	rec = recipe
	serving = rec.serving
	measurements = ["tablespoon", "tablespoons", "teaspoon", "teaspoon", "teaspoons", "pinch", "dash", "clove", "cloves"]
	spiceAmount = 0.25*serving
	first = Ingredient(str(Fraction(spiceAmount)) + " teaspoons ground cumin")
	second = Ingredient(str(Fraction(spiceAmount)) + " teaspoons ground cardamom")
	spiceTwoAmount = 0.125*serving
	third = Ingredient(str(Fraction(spiceTwoAmount)) + " pieces cinnamon stick")
	fourth = Ingredient(str(Fraction(spiceTwoAmount)) + " teaspoon ground turmeric")
	curryAmount = 0.5*serving
	fifth = Ingredient(str(Fraction(curryAmount)) + " tablespoons curry powder")
	indian_list = [first, second, third, fourth, fifth]
	bad_list = []

	for ingredient in recipe.food_list:
		if ingredient.getMeasurement() in measurements:
			bad = copy.deepcopy(ingredient)
			if ("water" not in bad.getName()):
				bad_list.append(bad.getName())
	new_list = []
	for ingredient in recipe.food_list:
		if ingredient.getName() not in bad_list:
			new_list.append(ingredient)
	recipe.food_list = new_list
	rec.food_list.extend(indian_list)

	for i in range(len(rec.food_list)):
		for ingredient in indian_substitutes.keys():
			if ingredient in rec.food_list[i].getName().lower():
				rec.food_list[i].data['name'] = indian_substitutes[ingredient]

	directions = rec.directions
	for i, direction in enumerate(directions):
		direction_lower = direction.lower()
		for ingredient in bad_list:
			if ingredient in direction:
				direction_lower = direction_lower.replace(ingredient, ingredient + " and spices")
				directions[i] = direction_lower
		for ingredient in indian_substitutes.keys():
			if ingredient in direction_lower:
				substitute = indian_substitutes[ingredient]
				direction_lower = direction_lower.replace(ingredient, substitute)
				directions[i] = direction_lower
	rec.directions = directions
	return rec

def MakeItalian(recipe):
	rec = recipe
	serving = int(rec.serving)
	measurements = ["tablespoon", "tablespoons", "teaspoon", "teaspoon", "teaspoons", "pinch", "dash", "clove", "cloves"]
	spiceAmount = 0.25*serving
	first = Ingredient(str(Fraction(spiceAmount)) + " teaspoons oregano")
	second = Ingredient(str(Fraction(spiceAmount)) + " teaspoons basil")
	spiceTwoAmount = 0.125*serving
	third = Ingredient(str(Fraction(spiceTwoAmount)) + " teaspoons thyme")
	fourth = Ingredient(str(Fraction(spiceTwoAmount)) + " teaspoons rosemary")
	curryAmount = 0.5*serving
	fifth = Ingredient(str(Fraction(curryAmount)) + " teaspoons parsley")
	italian_list = [first, second, third, fourth, fifth]
	bad_list = []

	for ingredient in recipe.food_list:
		if ingredient.getMeasurement() in measurements:
			bad = copy.deepcopy(ingredient)
			if ("water" not in bad.getName()):
				bad_list.append(bad.getName())
	new_list = []
	for ingredient in recipe.food_list:
		if ingredient.getName() not in bad_list:
			new_list.append(ingredient)
	recipe.food_list = new_list
	rec.food_list.extend(italian_list)

	for i in range(len(rec.food_list)):
		for ingredient in italian_substitutes.keys():
			if ingredient in rec.food_list[i].getName().lower():
				rec.food_list[i].data['name'] = italian_substitutes[ingredient]

	directions = rec.directions
	for i, direction in enumerate(directions):
		direction_lower = direction.lower()
		for ingredient in bad_list:
			if ingredient in direction:
				direction_lower = direction_lower.replace(ingredient, ingredient + " and herbs")
				directions[i] = direction_lower
		for ingredient in italian_substitutes.keys():
			if ingredient in direction_lower:
				substitute = italian_substitutes[ingredient]
				direction_lower = direction_lower.replace(ingredient, substitute)
				directions[i] = direction_lower
	rec.directions = directions
	return rec

def toHealthy(recipe):
	rec = recipe
	# replace in ingredients
	food_list = recipe.food_list
	for i in range(len(rec.food_list)):
		for ingredient in healthy_substitutes.keys():
			if ingredient in rec.food_list[i].getName().lower():
				rec.food_list[i].data['name'] = healthy_substitutes[ingredient]

	# replace in steps
	steps = recipe.directions
	for i, step in enumerate(steps):
		step_lower = step.lower()
		for ingredient in healthy_substitutes.keys():
			if ingredient in step_lower:
				substitute = healthy_substitutes[ingredient]
				step_lower = step_lower.replace(ingredient, substitute)
				steps[i] = step_lower
	rec.directions = steps
	return rec

def toUnhealthy(recipe):
	rec = recipe
	# replace in ingredients
	for i in range(len(rec.food_list)):
		for unhealthy, healthy in healthy_substitutes.iteritems():
			if healthy in rec.food_list[i].getName().lower():
				rec.food_list[i].data['name'] = unhealthy

	# replace in steps
	steps = recipe.directions
	for i, step in enumerate(steps):
		step_lower = step.lower()
		for unhealthy, healthy in healthy_substitutes.iteritems():
			if healthy in step_lower:
				step_lower = step_lower.replace(healthy, unhealthy)
				steps[i] = step_lower
	rec.directions = steps
	return rec
