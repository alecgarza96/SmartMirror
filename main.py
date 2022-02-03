import tkinter as tk
from SmartMirror.Weather import Weather
from SmartMirror.Location import Location
from SmartMirror.Time import Time
from SmartMirror.Date import Date
from SmartMirror.SmartMirror import SmartMirror
from SmartMirror.Quotes import Quotes

def getQuoteData(quotesLocation):
	quote = Quotes()
	quote.getQuotesJson(quotesLocation)
	quote.setTodaysQuote()

	return quote.getTodaysQuote()

def setupDisplay():
	root = tk.Tk()
	canvas = tk.Canvas(root, height=800, width=900)
	canvas.pack
	return root

if __name__ == '__main__':

	HEIGHT = 700
	WIDTH = 800

	loc = Location()
	city = loc.getCity()
	state = loc.getState()
	weather = Weather()
	quote = getQuoteData('SmartMirror/quotes.json')


	temperature = weather.get_temp(city,state) + " degrees"
	weatherReport = weather.get_report(city,state)
	time = Time().get_time()
	date = Date().get_date()

	root = setupDisplay()
	smartMirror = SmartMirror(root,temperature,quote['quote']+" - "+quote['author'],time,date)
	root.mainloop()



