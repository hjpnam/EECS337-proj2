import requests
from bs4 import BeautifulSoup

def get_ingredients(url):
	page = BeautifulSoup(requests.get(url))
	ingredients = []
	for ingredient in soup.find_all(itemprop="ingredients"):
		ingredients.append(ingredient.get_text())

def get_direction(url):
	pass //TODO
