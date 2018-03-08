from Vocabulary import *
from Ingredient import Ingredient
from Recipe import Recipe

def toVegetarian(recipe, vegOption):
	rec = recipe
	if vegOption.lower() not in vegetarian:
		return False
	for i in range(len(rec.food_list)):
		if(rec.food_list[i].getName().lower() in meat or rec.food_list[i].getName().lower() in fish):
			rec.food_list[i].data['name'] = vegOption
	return rec

def MakeIndian(recipe):
	rec = recipe
	measurements = ["tablespoon", "tablespoons", "teaspoon", "teaspoons", "pinch"]
	first = Ingredient("2 teaspoons ground cumin")
	second = Ingredient("1/2 teaspoon ground cardamom")
	third = Ingredient("1 piece cinnamon stick")
	fourth = Ingredient("1 teaspoon ground turmeric")
	indian_list = [first, second, third, fourth]

	for ingredient in rec.food_list:
		if ingredient.getMeasurement() in measurements:
			rec.food_list.remove(ingredient)
	rec.food_list.extend(indian_list)
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
		for ingredient in healthy_substitutes.keys():
			if ingredient in step.lower():
				substitute = healthy_substitutes[ingredient]
				step = step.replace(ingredient, substitute)
				steps[i] = step
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
				print healthy
				print unhealthy
				step_lower = step_lower.replace(healthy, unhealthy)
				steps[i] = step_lower
	rec.directions = steps
	return rec
