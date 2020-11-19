import board
import busio
import time 
import adafruit_mcp4725
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(0x48)
i2c = busio.I2C(board.SCL, board.SDA)
dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)

print('1 leer Voltage , 0 Cambiar voltaje')
read_or_write = int(input()) # 1 read  0 write

if read_or_write == 0 :
	print("¿Vout?")
	Vout = float(input())
	Vcod_out=int((Vout*65535)/5)
	dac.value =Vcod_out
	time.sleep(1)

else: 

	GAIN = 2/3

	print('Reading ADS1x15 values, press Ctrl-C to quit...')
	print('|     Canal {0:>6}     |       Canal {1:>6}   |'.format(*range(2)))
	print('-' * 37)

	values = [0]*2
	valuess = [0]*2
	for i in range(2):
		values[i] = adc.read_adc(i, gain=GAIN)
		valuess[i] = (values[i]*6.144)/32767
        
	print('| {0:>2} V | {1:>2} V |'.format(*valuess))
	time.sleep(0.5)
	valuess
