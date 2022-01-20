from Calendar import GoogleCalendar

TOKEN = '/Users/alecgarza/Desktop/SmartMirrorBackup/cfg/token.json'
cal = GoogleCalendar()
cal._getCreds(TOKEN)
print(cal.credentials)