from Vocabulary import *

def toVegetarian(recipe, vegOption):
	Recipe rec = recipe
	if vegOption.lower() not in vegetarian:
		return False
	for i in range(len(self.foodlist)):
		if(rec.foodlist[i].getName().lower() in meat or rec.foodlist[i].getName().lower() in fish):
			rec.foodlist[i].data['name'] = vegOption
	return rec
	
def MakeIndian(recipe):
	Recipe rec = recipe
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
