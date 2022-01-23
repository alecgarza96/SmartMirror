import unittest
from Calendar import GoogleCalendar

TOKEN = '/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json'

class TestCalendar(unittest.TestCase):

	def test__getCreds(self):
		cal = GoogleCalendar()
		self.assertIsNotNone(cal._getCreds('/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json'))
		self.assertIsNotNone(cal._getCreds(''))
		self.assertIsNotNone(cal._getCreds(0))
		self.assertIsNotNone(cal._getCreds(1))

if __name__ == '__main__':
	cal = GoogleCalendar()
	print("Passing 0", cal._getCreds(0))
	unittest.main()



