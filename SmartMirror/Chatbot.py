import speech_recognition as sr
from gtts import gTTS
from GCal import GoogleCalendar
import os
from datetime import date
from datetime import datetime

class ChatBot():

	def __init__(self, name):
		print("-- starting up", name, "--")
		self.name = name
		self.text = None

	def speech_to_text(self):
		recognizer = sr.Recognizer()
		with sr.Microphone() as mic:
			print("listening...")
			audio = recognizer.listen(mic)
		try:
			self.text = recognizer.recognize_google(audio)
			print("me --> ", self.text)
		except:
			print("me--> ERROR")

	def wake_up(self,text):
		return True if self.name or "sushi" in text.lower() else False

	@staticmethod
	def text_to_speech(text):
		print("ai-->", text)
		speaker = gTTS(text=text, lang='en', slow=False)
		speaker.save("res.mp3")
		os.system("afplay res.mp3")
		os.remove("res.mp3")

	@staticmethod
	def action_time():
		return datetime.now().time().strftime('%H:%M')
