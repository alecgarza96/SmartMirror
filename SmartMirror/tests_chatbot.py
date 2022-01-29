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