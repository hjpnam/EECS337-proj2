import requests
from bs4 import BeautifulSoup
import nltk
from Food import Food

class Recipe:
	def __init__(self, url):
		self.page = BeautifulSoup(requests.get(url).content, 'html.parser')
		self.ingredients = [ingredient.get_text() for ingredient in self.page.find_all(itemprop="ingredients")]
		self.directions = [direction.get_text() for direction in self.page.find_all(class_="recipe-directions__list--item")]
		self.tools = []
		self.methods = []
		self.foodlist = [Food(ingredient) for ingredient in self.ingredients]
		
	def toVegetarian(self, vegOption):
		vegetarian_options = ['seitan','lentil','tofu','mushroom']
		if vegOption.lower() not in vegetarian_options:
			return False
		for i in range(len(self.foodlist)):
			if(self.foodlist[i].isMeat):
				self.foodlist[i] = Food(vegOption)
		
		