import tkinter as tk
from SmartMirror.Weather import Weather
from SmartMirror.Location import Location
from SmartMirror.Time import Time
from SmartMirror.Date import Date

if __name__ == '__main__':

	HEIGHT = 700
	WIDTH = 800

	loc = Location()
	city = loc.getCity()
	state = loc.getState()
	weather = Weather()

	temperature = weather.get_temp(city,state) + " degrees"
	weatherReport = weather.get_report(city,state)
	time = Time().get_time()
	date = Date().get_date()

	root = tk.Tk()

	canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
	canvas.pack()

	frame = tk.Frame(root, bg='black')
	frame.place(relwidth=1, relheight=1)

	weatherLabel = tk.Label(frame, text=temperature, bg='black', fg='white')
	weatherLabel.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)

	gcalLabel = tk.Label(frame, text=weatherReport, bg='black', fg='white')
	gcalLabel.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)

	quoteLabel = tk.Label(frame, text="Quotes go here", bg='black', fg='white')
	quoteLabel.place(relx=0.7, rely=0.7, relwidth=0.2, relheight=0.1)

	wordLabel = tk.Label(frame, text="Word of the day goes here", bg='black', fg='white')
	wordLabel.place(relx=0.7, rely=0.8, relwidth=0.2, relheight=0.1)

	timeLabel = tk.Label(frame, text=time, bg='black', fg='white')
	timeLabel.place(relx=0.1, rely=0.7, relwidth=0.2, relheight=0.1)

	dateLabel = tk.Label(frame, text=date, bg='black', fg='white')
	dateLabel.place(relx=0.1, rely=0.8, relwidth=0.2, relheight=0.1)

	root.mainloop()


"""
google calendar test code

from Chatbot import ChatBot
from GCal import GoogleCalendar

def loginToCalendar():
	cal = GoogleCalendar()
	cal._getCreds()
	cal._userlogin()
	return cal

def getNextEventName(calendar):
	return calendar.getEvents()[0]['summary']

if __name__ == '__main__':

	event = getNextEventName(loginToCalendar())
	ai = ChatBot(name="Fushi")

	while True:
		ai.speech_to_text()

		if ai.wake_up(ai.text) is True:
			res = "Hello"

		if "calendar" in ai.text:
			res = event

		ai.text_to_speech(res)
		ai.text = None
"""
