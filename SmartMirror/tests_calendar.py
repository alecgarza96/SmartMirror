import unittest
from Calendar import GoogleCalendar

TOKEN = '/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json'

class TestCalendar(unittest.TestCase):

	def test__getCreds(self):
		result = GoogleCalendar._getCreds('/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json')
		self.assertIsNotNone(result)

if __name__ == '__main__':
	unittest.main()


