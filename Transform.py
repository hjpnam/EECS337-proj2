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
	for i in range(len(rec.food_list)):
		if(rec.food_list[i].getName().lower() in meat or rec.food_list[i].getName().lower() in fish):
			rec.food_list[i].data['name'] = vegOption
	return rec

def MakeIndian(recipe):
	rec = recipe
	serving = int(rec.serving)
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
			#bad_list.append(bad.getName())
	new_list = []
	for ingredient in recipe.food_list:
		if ingredient.getName() not in bad_list:
			new_list.append(ingredient)
	recipe.food_list = new_list
	rec.food_list.extend(indian_list)

	#Food list has replaced spices with indian spices
	#Next step: replacing directions
	#Look for each word in each ingredient individually
	#If any of them removed, replace with "spices" or ""
	#Replace with spices the first time in that direction you encounter a removed ingredient

	new_directions = []
	directions = rec.directions
	for direction in directions:
		changed = False
		for ingredient in bad_list:
			text = nltk.word_tokenize(ingredient)
			for word in text:
				if word in direction:
					mystring = str(word)
					if changed == False:
						direction = direction.replace(mystring, "spices")
						changed = True
					if changed == True:
						direction = direction.replace(mystring, '') #Simply remove the ingredient
						direction = direction.replace("  ,", '') #String Cleanup
						direction = direction.replace(" and  ", ' ')
						direction = direction.replace(",  .", '.')
						direction = direction.replace(", ,   .", '.')
		new_directions.append(direction)
	rec.directions = new_directions
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
	indian_list = [first, second, third, fourth, fifth]
	bad_list = []

	for ingredient in recipe.food_list:
		if ingredient.getMeasurement() in measurements:
			bad = copy.deepcopy(ingredient)
			if ("water" not in bad.getName()):
				bad_list.append(bad.getName())
			#bad_list.append(bad.getName())
	new_list = []
	for ingredient in recipe.food_list:
		if ingredient.getName() not in bad_list:
			new_list.append(ingredient)
	recipe.food_list = new_list
	rec.food_list.extend(indian_list)

	#Food list has replaced spices with indian spices
	#Next step: replacing directions
	#Look for each word in each ingredient individually
	#If any of them removed, replace with "spices" or ""
	#Replace with spices the first time in that direction you encounter a removed ingredient

	new_directions = []
	directions = rec.directions
	for direction in directions:
		changed = False
		for ingredient in bad_list:
			text = nltk.word_tokenize(ingredient)
			for word in text:
				if word in direction:
					mystring = str(word)
					if changed == False:
						direction = direction.replace(mystring, "spices")
						changed = True
					if changed == True:
						direction = direction.replace(mystring, '') #Simply remove the ingredient
						direction = direction.replace("  ,", '') #String Cleanup
						direction = direction.replace(" and  ", ' ')
						direction = direction.replace(",  .", '.')
						direction = direction.replace(", ,   .", '.')
		new_directions.append(direction)
	rec.directions = new_directions
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
				print (healthy)
				print (unhealthy)
				step_lower = step_lower.replace(healthy, unhealthy)
				steps[i] = step_lower
	rec.directions = steps
	return rec

mine = Recipe("https://www.allrecipes.com/recipe/151266/boneless-buffalo-wings/")
MakeItalian(mine)
print(mine.directions)
print(mine.food_list)
