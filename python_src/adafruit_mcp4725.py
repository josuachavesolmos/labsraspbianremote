#adafruit_mcp4725
class MCP4725():
	def __init__(self,i2c,address):
		self.i2c=i2c
		self.address=address
		self.value=0