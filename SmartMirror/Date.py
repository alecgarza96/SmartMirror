from datetime import date
from datetime import datetime

class Date():

	def __init__(self):
		self.today = None
		self.time = None

	def get_date(self):
		self.today = date.today()
		return self.today



