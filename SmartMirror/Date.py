from datetime import date
from datetime import datetime

class Date():

	def __init__(self):
		self.today = None
		self.month = None
		self.year = None
		self.date = None
		self.monthMapping = {"01": "January",
		                     "02": "February",
		                     "03": "March",
		                     "04": "April",
		                     "05": "May",
		                     "06": "June",
		                     "07": "July",
		                     "08": "August",
		                     "09": "September",
		                     "10": "October",
		                     "11": "November",
		                     "12": "December"}

	def _get_date(self):
		self.today = str(date.today())

	def get_date(self):
		self._get_date()
		self.month = self.monthMapping[self.today[5:7]]
		self.year = self.today[0:4]
		self.date = self.today[9:10]

		date = self.month + " " + self.date + ", " + self.year
		return date

		



