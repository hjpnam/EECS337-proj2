from Vocabulary import *
from Ingredient import Ingredient
from Recipe import Recipe
import copy
import nltk
from fractions import Fraction

def toVegetarian(recipe):
	rec = recipe
	steps = rec.directions
	food_list = rec.food_list
	serving = rec.serving
	
	for i in range(len(food_list)):
		for m in meat_priority.keys():
			if m in food_list[i].getName():
				food_list[i].data['name'] = meat_priority[m]
				
		for m in meat:
			if m in food_list[i].getName():
				food_list[i].data['name'] = meat[m]
				food_list[i].data['measurement'] = str(vegetarian_attribute[meat[m]]['measurement'])
				food_list[i].data['quantity'] = str(vegetarian_attribute[meat[m]]['servingSize']*serving)
				food_list[i].data['descriptor'] = []
				food_list[i].data['preparation'] = 'none'
				
		for f in fish:
			if f in food_list[i].getName():
				food_list[i].data['name'] = 'tofu'
				food_list[i].data['measurement'] = str(vegetarian_attribute['tofu']['measurement'])
				food_list[i].data['quantity'] = str(vegetarian_attribute['tofu']['servingSize']*serving)
				food_list[i].data['descriptor'] = []
				food_list[i].data['preparation'] = 'none'
				
	for i in range(len(steps)):
		step_lower = steps[i].lower()
		for m in meat_priority.keys():
			if m in step_lower:
				step_lower = step_lower.replace(m, meat_priority[m])
		for m in meat:
			if m in step_lower:
				step_lower = step_lower.replace(m, meat[m])
				steps[i]=step_lower
		for f in fish:
			if f in step_lower:
				step_lower = step_lower.replace(f, 'tofu')
				steps[
		for trash in meat_trash:
			if trash in step_lower:
				step_lower = step_lower.replace(trash, '')
				steps[i]=step_lower
	rec.food_list = food_list
	rec.directions = steps
	return rec
	
def fromVegetarian(recipe):
	

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

	new_food_list = recipe.food_list
	if len(bad_list) >= 1:
		new_food_list.extend(indian_list)
	rec.food_list = new_food_list
	for i in range(len(rec.food_list)):
		for ingredient in indian_substitutes.keys():
			if ingredient in rec.food_list[i].getName().lower():
				rec.food_list[i].data['name'] = indian_substitutes[ingredient]

	directions = rec.directions
	for i, direction in enumerate(directions):
		direction_lower = direction.lower()
		for ingredient in bad_list:
			ingredient_lower = ingredient.lower()
			if ingredient_lower in direction:
				direction_lower = direction_lower.replace(ingredient_lower, ingredient_lower + " and spices")
				directions[i] = direction_lower
				break;
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

	new_food_list = recipe.food_list
	if len(bad_list) >= 1:
		new_food_list.extend(italian_list)
	rec.food_list = new_food_list

	for i in range(len(rec.food_list)):
		for ingredient in italian_substitutes.keys():
			if ingredient in rec.food_list[i].getName().lower():
				rec.food_list[i].data['name'] = italian_substitutes[ingredient]

	directions = rec.directions
	for i, direction in enumerate(directions):
		direction_lower = direction.lower()
		for ingredient in bad_list:
			if ingredient in direction:
				ingredient_lower = ingredient.lower()
				direction_lower = direction_lower.replace(ingredient_lower, ingredient_lower + " and herbs")
				directions[i] = direction_lower
				break;
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
