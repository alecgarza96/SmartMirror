import json

class Quotes():

	def __init__(self):
		self.quote = " "
		self.quotesJson = None
		self.currentCounter = 0

	def getQuotesJson(self, quotesJson):
		file = open(quotesJson)
		self.quotesJson = json.load(file)
		file.close()

	def _checkCounter(self):
		if(self.currentCounter == len(self.quotesJson)):
			self.currentCounter == 0

	def _setQuote(self):
		if(self.quotesJson):
			self.quote = self.quotesJson['quotes'][self.currentCounter]
			self.currentCounter += 1

	def setTodaysQuote(self):
		self._checkCounter()
		self._setQuote()

	def getTodaysQuote(self):

		return self.quote



