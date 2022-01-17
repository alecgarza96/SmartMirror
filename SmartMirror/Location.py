import geocoder

class Location():
	user = 'me'

	def __init__(self, user=user):
		self.loc = geocoder.ip(user)
		
	def getCity(self):
		return self.loc.city 

	def getState(self):
		return self.loc.state 
