import requests
from bs4 import BeautifulSoup

class Recipe:
	def __init__(self, url):
		self.page = BeautifulSoup(requests.get(url).content, 'html.parser')
		self.ingredients = [ingredient.get_text() for ingredient in soup.find_all(itemprop="ingredients")]
		self.directions = [direction.get_text() for direction in soup.find_all(class_="recipe-directions__list--item")]
		self.tools = []
		self.methods = []