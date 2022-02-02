import json

class Quotes():

	def __init__(self, quotes=None):
		self.today = " "
		self.quotesDict = quotes



file = open('quotes.json')

quotes = json.load(file)

"""
for i in quotes['quotes']:
	print(i)
	"""

print(quotes['quotes'][0])

print(len(quotes['quotes']))