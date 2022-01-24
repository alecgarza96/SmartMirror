import requests
import json

class Weather():

	def __init__(self):
		self._BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
		self._API_KEY = "9cbb8f5c607b163d50f8454ae4af0af5"

	def get_temp(self, city, state):
		temperatureResponse = ' '
		URL = self._BASE_URL + "q=" + city + "," + state + "&appid=" + self._API_KEY
		response = requests.get(URL)

		if(response.status_code == 200):
			data = response.json()
			main = data['main']
			temperatureResponse = str(int((((float(main['temp'])-273.15)*9)/5)+32))

		return temperatureResponse

	def get_report(self, city, state):
		reportResponse = "Error: Weather API Connection Issue"
		URL = self._BASE_URL + "q=" + city + "," + state + "&appid=" + self._API_KEY
		response = requests.get(URL)

		if(response.status_code == 200):
			data = response.json()
			main = data['main']
			report = data['weather']
			reportResponse = report[0]['description']

		return reportResponse


