from datetime import datetime

class Time():

	def __init__(self):
		self.time = None

	def get_time(self):
		self.time = datetime.now()
		return self.time.strftime("%H:%M:%S")