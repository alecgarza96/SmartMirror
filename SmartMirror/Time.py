from datetime import datetime

class Time():

	def __init__(self):
		self.time = None
		self._get_time()
		self._format_time()

	def _get_time(self):
		self.time = datetime.now().time().strftime("%H:%M:%S")
		return self.time

	def _format_time(self):
		self._get_time()
		if(self.time[0:2] == "00"):
			formattedTime = "12"+self.time[2:]
			self.time = formattedTime
		else if(int(self.time[0:2]) < 12):
			self.time = self.time[0:5]
		else:
			hour = int(self.time[0:2])-12
			formattedTime = str(hour)+self.time[2:]
			self.time = formattedTime

	def get_time(self):
		return self.time





