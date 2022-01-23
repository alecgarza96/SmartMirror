import unittest
from Calendar import GoogleCalendar

TOKEN = '/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json'

class TestCalendar(unittest.TestCase):

	def test__getCreds(self):
		cal = GoogleCalendar()
		self.assertIsNotNone(cal._getCreds('/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json'))
		self.assertIsNotNone(cal._getCreds(''))
		self.assertIsNotNone(cal._getCreds(0))
		self.assertIsNotNone(cal._getCreds(-1))

	def test_checkCredentialsExpired(self):
		cal = GoogleCalendar()
		validToken = cal._getCreds('/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json')
		emptyToken = cal._getCreds('')
		self.assertFalse(cal._checkCredentialsExpired(validToken))
		self.assertTrue(cal._checkCredentialsExpired(emptyToken))

if __name__ == '__main__':
	unittest.main()



