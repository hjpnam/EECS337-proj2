import requests
from bs4 import BeautifulSoup
import nltk
from Ingredient import Ingredient
from Vocabulary import *

class Recipe:
	def __init__(self, url):
		self.page = BeautifulSoup(requests.get(url).content, 'html.parser')
		ingredients = [ingredient.get_text().encode('utf-8') for ingredient in self.page.find_all(itemprop="ingredients")]
		self.directions = [direction.get_text().encode('utf-8') for direction in self.page.find_all(class_="recipe-directions__list--item")]
		self.tools = self.find_tools()
		self.primary_methods = self.get_primary_methods()
		self.other_methods = self.get_other_methods()
		self.food_list = [Ingredient(i) for i in ingredients]
#		for i in self.food_list:
	#		print (i.getData()['name'])
		self.serving = self.page.find(id='metaRecipeServings').get('content')

	def find_tools(self):
		directions = self.directions
		stopwords = ["boil", "heat", "sauce", "egg", "mixture", "oil", "blend", "chicken"]
		nouns = []
		for direction in directions:
			text = nltk.word_tokenize(direction)
			parsed = nltk.pos_tag(text)
			for i in range(len(parsed)):
				if (parsed[i][0] == "in" or parsed[i][0] == "to"):
					if (parsed[i+1][0] == "a" or parsed[i+1][0] == "the"):
						spot = i
						end = (i+5 if (i+5 < len(parsed)) else len(parsed))
						tool = []
						while (spot<end):
							if (parsed[spot][1] == "NN"):
								if (parsed[spot][0] not in stopwords):
									tool.append(parsed[spot][0])
							spot += 1
						if (len(tool)>0): nouns.append(' '.join(tool))
		return set(nouns)

	def get_primary_methods(self):
		steps = self.directions
		primary_methods_found = []
		for step in steps:
			for method in primary_methods:
				if method in step.lower():
					primary_methods_found.append(method)
				elif method + "ing" in step.lower():
					method = method[:-3]
					primary_methods_found.append(method)
				elif method + "ed" in step.lower():
					method = method[:-2]
					primary_methods_found.append(method)
				elif method + "d" in step.lower():
					method = method[:-1]
					primary_methods_found.append(method)
				elif method + "s" in step.lower():
					method = method[:-1]
					primary_methods_found.append(method)
		return list(set(primary_methods_found))

	def get_other_methods(self):
		steps = self.directions
		other_methods_found = []
		for step in steps:
			for method in other_methods:
				if method in step.lower():
					other_methods_found.append(method)
				elif method + "ing" in step.lower():
					method = method[:-3]
					other_methods_found.append(method)
				elif method + "ed" in step.lower():
					method = method[:-2]
					other_methods_found.append(method)
				elif method + "d" in step.lower():
					method = method[:-1]
					primary_methods_found.append(method)
				elif method + "s" in step.lower():
					method = method[:-1]
					primary_methods_found.append(method)
		return list(set(other_methods_found))

	def __str__(self):
		food_list_str = [str(food) for food in self.food_list]
		str_form = "\nIngredients:\n"
		for food in food_list_str:
			str_form += (food+"\n")
		str_form += "\n\n"
		str_form += "Follow these instructions fool\n"
		for direction in self.directions:
			str_form += (direction+"\n")
		return str_form
