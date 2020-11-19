import random

class ADS1115:
	def __init__(self,address):
		self.address=address

	def read_adc(self,i,gain):
		return random.randint(0,32767)