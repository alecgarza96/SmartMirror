from datetime import datetime

class Time():

	def __init__(self):
		self.time = None

	def _get_time(self):
		self.time = datetime.now()
		return self.time.strftime("%H:%M:%S")

	def _format_time(self):
		time = self._get_time()
		