import unittest
from Calendar import GoogleCalendar

TOKEN = '/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json'

class TestCalendar(unittest.TestCase):

	def test__getCreds(self):
		cal = GoogleCalendar()
		cal._getCreds('/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json')
		self.assertIsNotNone(cal.credentials)

		emptyStringCal = GoogleCalendar()
		cal._getCreds('')
		self.assertIsNotNone(emptyStringCal.credentials)

if __name__ == '__main__':
	unittest.main()


