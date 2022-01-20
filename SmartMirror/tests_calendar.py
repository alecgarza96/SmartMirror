from Calendar import GoogleCalendar

TOKEN = '/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json'
cal = GoogleCalendar()

print("Unit Testing for GoogleCalendar")
print("-------------------------------")

print("Testing: _getCreds()")
cal._getCreds(TOKEN)
print("Credentials Found:", cal.credentials)
print('\n')

print("Testing: _checkCredentialsExpired()")
print("Credentials Expiration Status:", cal._checkCredentialsExpired())
print('\n')