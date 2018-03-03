from Ingredient import Ingredient

def MakeIndian(food_list):
    measurements = ["tablespoon", "tablespoons", "teaspoon", "teaspoons", "pinch"]
    first = Ingredient("2 teaspoons ground cumin")
    second = Ingredient("1/2 teaspoon ground cardamom")
    third = Ingredient("1 piece cinnamon stick")
    fourth = Ingredient("1 teaspoon ground turmeric")
    indian_list = [first, second, third, fourth]

    for ingredient in food_list:
        if ingredient.getMeasurement() in measurements:
            food_list.remove(ingredient)
    food_list.extend(indian_list)
    return food_list

obj1 = Ingredient("1 tablespoon dried thyme")
obj2 = Ingredient("4 skinless, boneless chicken breast")

food_list = [obj1, obj2]

food_list = MakeIndian(food_list)
print(food_list[2].getData())
