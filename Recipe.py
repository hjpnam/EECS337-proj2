import requests
from bs4 import BeautifulSoup
import nltk

class Recipe:
	def __init__(self, url):
		self.page = BeautifulSoup(requests.get(url).content, 'html.parser')
		self.ingredients = [ingredient.get_text() for ingredient in self.page.find_all(itemprop="ingredients")]
		self.directions = [direction.get_text() for direction in self.page.find_all(class_="recipe-directions__list--item")]
		self.tools = []
		self.methods = []

	def find_tools(self):
		directions = self.directions
		nouns = []
		for direction in directions:
			text = nltk.word_tokenize(direction)
			parsed = nltk.pos_tag(text)
			for i in range(len(parsed)):
				if (parsed[i][0] == "in" or parsed[i][0] == "to"):
					if (parsed[i+1][0] == "a" or parsed[i+1][0] == "the"):
						spot = i
						end = i+5
						tool = []
						while (spot<end):
							if (parsed[spot][1] == "NN"):
								if (parsed[spot][0] != "boil" and parsed[spot][0] != "heat"):
									tool.append(parsed[spot][0])
							spot += 1
						if (len(tool)>0): nouns.append(tool)
		return nouns
