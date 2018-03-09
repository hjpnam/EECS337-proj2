from Recipe import Recipe
from Transform import *
import sys

#printing recipe objects won't print pretty at the moment. need to prettify
def main():
	if len(sys.argv) == 2:
		recipe = Recipe(argv[1])
		option = input("Enter 1 for Healthier, 2 for Indian, 3 for Vegetarian: ")
		if option == 1:
			print (toHealthy(recipe))
		elif option == 2:
			print (MakeIndian(recipe))
		elif option == 3:
			print(toVegetarian(recipe))
		else:
			print ("invalid input")
	else:
		print("wrong number of arguments")

main()
