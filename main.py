from Recipe import Recipe
from Transform import *
import sys

def main():
	if len(sys.argv) == 2:
		if sys.argv[1][0:4] != "http":
			print ("Invalid url, missing http")
			return
		recipe = Recipe(sys.argv[1])
		option = int(input("Enter 1 for Healthier, 2 for Indian, 3 for Italian, 4 for toVegetarian, 5 for Unhealthier, 6 for fromVegetarian: "))
		if option == 1:
			print (toHealthy(recipe))
		elif option == 2:
			print (MakeIndian(recipe))
		elif option == 3:
			print (MakeItalian(recipe))
		elif option == 4:
			print (toVegetarian(recipe))
		elif option == 5:
			print (toUnhealthy(recipe))
		elif option == 6:
			print (fromVegetarian(recipe))
		else:
			print ("invalid input")
	else:
		print("wrong number of arguments")

main()
