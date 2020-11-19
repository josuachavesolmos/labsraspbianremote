import board
import busio
import time 
import adafruit_mcp4725
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115(0x48)
i2c = busio.I2C(board.SCL, board.SDA)
dac = adafruit_mcp4725.MCP4725(i2c, address=0x60)
dac2 = adafruit_mcp4725.MCP4725(i2c, address=0x62)
GAIN = 2/3

def set_V(Vout):
    Vcod_out=int((Vout*65535)/5)
    dac.value =Vcod_out
    dac2.value =Vcod_out

def readADC(): 
    values = [0]*4
    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN)
        values[i] = (values[i]*6.144)/32767
    return values

if __name__ == '__main__':
    print('1 leer Voltage , 0 Cambiar voltaje')
    read_or_write = int(input())
    if read_or_write == 0:
        print("¿Vout?")
        Vout = float(input())
        set_V(Vout)
    else:
        print('Reading ADS1x15 values, press Ctrl-C to quit...')
        print('|     Canal {0:>6}     |       Canal {1:>6}   |       Canal {2:>6}   |       Canal {3:>6}   |'.format(*range(4)))
        print('-' * 37)
        valuess=readADC()
        print('| {0:>4} V | {1:>4} V | {2:>4} V | {3:>4} V |'.format(*valuess))